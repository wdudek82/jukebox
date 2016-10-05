import csv
from collections import namedtuple

from django.core.management.base import BaseCommand, CommandError
from playlist.models import Genre


class Command(BaseCommand):
    help = 'Imports soundcodes from csv files to database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        cli_c = namedtuple('CLIc', ['close', 'red', 'green'])
        msg = cli_c('\033[0m', '\033[0;31m', '\033[0;32m')

        # with open(options['csv_file'], newline='') as csv_file:
        with open(options['csv_file']) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=';')

            count = 1
            for row in csv_data:
                genre_name = row[1].title()
                genre_code = row[0]

                genre, created = Genre.objects.get_or_create(
                    genre_name=genre_name,
                    genre_code=genre_code,
                )

                created = '{}{}{}'.format(msg[2 if created else 1], created, msg[0])
                print('[{:03}][{}] {} -> {}'.format(count, created, genre_code, genre_name))
                count += 1
