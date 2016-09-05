import csv
from collections import namedtuple

from django.core.management.base import BaseCommand, CommandError
from playlist.models import Soundcode


class Command(BaseCommand):
    help = 'Imports soundcodes from csv files to database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        cli_c = namedtuple('CLIc', ['close', 'red', 'green'])
        msg = cli_c('\033[0m', '\033[0;31m', '\033[0;32m')

        with open(options['csv_file'], newline='') as f:
            csv_data = csv.reader(f, delimiter=';')

            count = 1
            for row in csv_data:
                symbol = row[0]
                genre = row[1].title()

                soundcode, created = Soundcode.objects.get_or_create(
                    symbol=symbol,
                    genre=genre
                )

                created = '{}{}{}'.format(msg[2 if created else 1], created, msg[0])
                print('[{:03}][{}] {} -> {}'.format(count, created, symbol, genre))
                count += 1
