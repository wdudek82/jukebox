import csv
from collections import namedtuple
import logging

from django.core.management.base import BaseCommand, CommandError
from playlist.models import Category


class Command(BaseCommand):
    help = 'Imports track categories from csv files to database'

    logging.basicConfig(
        level=logging.DEBUG,
        format=' %(asctime)s - %(levelname)s - %(message)s'
    )

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        cli_c = namedtuple('CLIc', ['close', 'red', 'green'])
        msg = cli_c('\033[0m', '\033[0;31m', '\033[0;32m')

        with open(options['csv_file']) as csv_file:
            csv_data = csv.reader(csv_file, delimiter=';')

            count = 1
            for row in csv_data:
                if count == 1:
                    count += 1
                    continue
                category_name = row[1].title()
                category_code = row[0]

                category, created = Category.objects.get_or_create(
                    category_code=category_code
                )
                category.category_name = category_name
                category.save()

                created = '{}{}{}'.format(msg[2 if created else 1], created, msg[0])
                logging.debug('[{:03}][{}] {} -> {}'.format(count, created, category_code, category_name))
                count += 1
