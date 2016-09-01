import os

from jukebox.settings import BASE_DIR
from playlist.models import Soundcode


from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Imports playlists from *.csv files to database'

    def handle(self, *args, **options):
        path = os.path.join(BASE_DIR, 'data', 'soundcodes.csv')
        with open(path, 'r') as f:
            codes = f.readlines()

        imported = 0
        code_count = len(codes)
        for code in codes:
            code = code.split(';')
            symbol = code[0]
            title = code[1]

            if (symbol and len(symbol) == 1) and title:
                soundcode, created = Soundcode.objects.get_or_create(title=title, symbol=symbol)

                soundcode.save()
                print('[ {} ] {}: {}'.format(created, symbol, title))
                imported += 1 if created else 0

        print('Imported codes: {} of {}'.format(imported, code_count))