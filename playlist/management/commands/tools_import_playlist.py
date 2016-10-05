import os
from collections import namedtuple
import logging
import discogs_client
import requests
import json
from PIL import Image

# from django.conf.global_settings import MEDIA_ROOT
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError, IntegrityError
from playlist.models import Album, Artist, Category, Genre, Track


class Command(BaseCommand):
    help = 'Imports playlist from csv files to database'

    cli_c = namedtuple('CLIc', ['close', 'red', 'green'])
    msg = cli_c('\033[0m', '\033[0;31m', '\033[0;32m')

    logging.basicConfig(
        filename=os.path.join('var', 'log', 'import_playlist__error.txt'),
        level=logging.ERROR,
        format=' %(asctime)s - %(levelname)s - %(message)s'
    )

    @staticmethod
    def error_logger(error):
        logging.error(error)

    def add_album(self, song_id, song_title, artists):
        artist_query = ', '.join(artists).lower()
        track_query = song_title.lower()

        USER_TOKEN = 'wYMnnQcqCxNHiOObpHaiBmNJHWzJFTnrTaTGXRSQ'

        client = discogs_client.Client('techcave-jukebox/0.8', user_token=USER_TOKEN)

        query = '{} {}'.format(track_query, artist_query)
        results = client.search(query, type='release')
        albums_list = [result for result in results]

        try:
            album_title = results[0].master.title
        except (IndexError, AttributeError):
            album_title = albums_list[0].title if albums_list else song_id

        cover_image_name = song_id+'.MP3.jpg'
        cover_image_path = os.path.join('covers', cover_image_name)

        album, created = Album.objects.get_or_create(title=album_title)
        album.cover_image = cover_image_path

        if albums_list:
            album.published_at = albums_list[0].year
        album.save()

        return album.id

    @staticmethod
    def add_artists(song, artists):
        for artist_name in artists:
            if artist_name == '':
                continue
            try:
                artist_name = artist_name.title().replace('_', ' ')
                artist, created = Artist.objects.get_or_create(name=artist_name)
                song.artists.add(artist.id)
            except ObjectDoesNotExist as e:
                logging.error('Error: {} -> {}'.format(e, artist_name))

    @staticmethod
    def add_category(category_code):
        category, created = Category.objects.get_or_create(category_code=category_code)
        return category.id

    @staticmethod
    def add_genres(track, genre_code_list):
        for genre_code in genre_code_list:
            try:
                genre_id = Genre.objects.get(genre_code=genre_code).id
                track.genres.add(genre_id)
            except ObjectDoesNotExist as e:
                logging.error('{Error: {} -> {}'.format(e, genre_code))

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):

        with open(options['csv_file']) as csv_file:
            csv_data = csv_file.readlines()

            count = 1
            for row in csv_data[1:]:
                row = row.split(';')

                # try:
                song_id = row[0]
                category_code = self.add_category(row[1])
                song_url = 'http://techcave.pl/{}.mp3'.format(song_id)
                song_title = row[4].title()
                artists = [row[2], row[3]]
                album_id = self.add_album(song_id, song_title, artists)
                genre_code_list = row[5]
                mood = int(row[6]) if row[6] else 1
                energy = int(row[7]) if row[7] else 1
                tempo = row[8].strip()

                track, track_created = Track.objects.get_or_create(
                    song_id=song_id,
                    category_id=category_code,
                    album_id=album_id,
                )

                track.song_url = song_url
                track.title = song_title
                track.album_id = album_id
                track.mood = mood
                track.energy = energy
                track.tempo = tempo
                track.save()

                # if track_created:
                self.add_genres(track, genre_code_list)
                self.add_artists(track, artists)

                track_created = '{}{}{}'.format(self.msg[2 if track_created else 1], track_created, self.msg[0])

                print('[{0:05}][ {1} ] {2} {3}'.format(count, track_created, song_id, song_title, album_id))

                count += 1

                # except AttributeError: as e:
                #     self.error_logger(e)
                # except IntegrityError as e:
                #     self.error_logger(e)
                # except DatabaseError as e:
                #     self.error_logger(e)
                # except AttributeError as e:
                #     self.error_logger(e)
