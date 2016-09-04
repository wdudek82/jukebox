import csv
from collections import namedtuple

from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from playlist.models import Album, Artist, Soundcode, Song


class Command(BaseCommand):
    help = 'Imports playlist from csv files to database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        CLIc = namedtuple('CLIc', ['close', 'red', 'green'])
        msg = CLIc('\033[0m', '\033[0;31m', '\033[0;32m')

        def add_artist(artist):
            artist, created = Artist.objects.get_or_create(
                name=artist,
            )
            return (artist, created)

        def add_album(song_id, album):
            cover_fname = '{}.MP3.jpg'.format(song_id)
            album, created = Album.objects.get_or_create(
                album_title=album,
                # cover=os.path.join(MEDIA_ROOT, 'covers', cover_fname)
                cover=cover_fname
            )

        def add_soundcodes(song, soundcodes):
            for code in soundcodes:
                try:
                    code = Soundcode.objects.get(symbol=code)
                    song.soundcode.add(code.id)
                except ObjectDoesNotExist as e:
                    error_msg = '{}ERROR{}'.format(msg[1], msg[0])
                    print('{0}: {1} -> "{2}"'.format(error_msg, e, code))

        with open(options['csv_file']) as f:
            csv_data = f.readlines()

            count = 1
            for row in csv_data[1:]:
                row = row.split(';')

                song_id = row[0]
                artist_1 = row[2]
                artist_2 = row[3]
                song_title = row[4]
                album = 1
                soundcodes = row[5]
                mood = int(row[6]) if row[6] else 1
                energy = int(row[7]) if row[7] else 1
                tempo = row[8].strip()

                artist_1, a1_created = add_artist(artist_1)
                artist_2, a2_created = add_artist(artist_2) if artist_2 else ('-', False)

                album = add_album(song_id, album)

                song, s_created = Song.objects.get_or_create(
                    song_id=song_id,
                    artist_1_id=artist_1.id,
                    artist_2_id=artist_2.id if a2_created else None,
                    song_title=song_title,
                    album_id=1,
                    mood=mood,
                    energy=energy,
                    tempo=tempo,
                )

                if s_created:
                    add_soundcodes(song, soundcodes)

                s_created = '{}{}{}'.format(msg[2 if s_created else 1], s_created, msg[0])
                print('[{0:05}][ {1} ] {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(
                    count, s_created, song_id, artist_1, artist_2, song_title,
                    Album.objects.get(id=1), soundcodes, mood, energy, tempo)
                )
                count += 1