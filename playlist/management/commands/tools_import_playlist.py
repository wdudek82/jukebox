from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Imports playlists from *.csv files to database'

    def handle(self, *args, **options):
        pass