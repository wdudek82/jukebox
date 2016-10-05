import requests
from collections import namedtuple
import logging
import json

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from playlist.models import Album, Track


class Command(BaseCommand):
    help = 'Imports track albums from external API'

    # logging.basicConfig(
    #     level=logging.DEBUG,
    #     format=' %(asctime)s - %(levelname)s - %(message)s'
    # )

    # def add_arguments(self, parser):
    #     parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        cli_c = namedtuple('CLIc', ['close', 'red', 'green'])
        msg = cli_c('\033[0m', '\033[0;31m', '\033[0;32m')

        api_url = 'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&'
        api_key = 'api_key=c3859c58dcd1870aad422a4779a35372'
        api_response_format='&format=json'

        tracks = Track.objects.all()
        for track in tracks:
            if track.album.title == track.song_id:
                artist_query = '&artist=' + track.artists.all()[0].name.replace(' ', '+')
                track_query = '&track=' + track.song_title.replace(' ', '+')

                api_request = '{}{}{}{}{}'.format(
                    api_url, api_key, artist_query.lower(), track_query.lower(), api_response_format
                )
                track_album_request = requests.get(api_request).content
                # print('[ {} ] {}'.format(str(track_album.status_code), track_album.content))

                track_album_response = json.loads(track_album_request)

                album_title = track_album_response.get('track', {}).get('album', {}).get('title')

                if album_title:
                    album = Album.objects.get(id=track.album.id)
                    try:
                        album.title = album_title
                        album.save()
                        print('====', album_title)
                    except IntegrityError:
                        album.delete()
                        album = Album.objects.get(title=album_title)
                        track.album_id = album.id
                        track.save()
                        print('====', track.album)
                else:
                    print('None')











        # with open(options['csv_file']) as csv_file:
        #     csv_data = csv.reader(csv_file, delimiter=';')
        #
        #     count = 1
        #     for row in csv_data:
        #         if count == 1:
        #             count += 1
        #             continue
        #         category_name = row[1].title()
        #         category_code = row[0]
        #
        #         category, created = Category.objects.get_or_create(
        #             category_code=category_code
        #         )
        #         category.category_name = category_name
        #         category.save()
        #
        #         created = '{}{}{}'.format(msg[2 if created else 1], created, msg[0])
        #         logging.debug('[{:03}][{}] {} -> {}'.format(count, created, category_code, category_name))
        #         count += 1
