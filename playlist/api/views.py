from rest_framework import generics

from playlist.api.serializers import AlbumSerializer, ArtistSerializer, SoundcodeSerializer, SongSerializer
from playlist.models import Album, Artist, Soundcode, Song


class Mixins:
    @classmethod
    def validate_timestamp(cls, timestamp):
        try:
            # datetime.strptime(timestamp[:11], '%YYYY-%mm-%dd')
            timestamp = timestamp.split('-')
            length = len(timestamp) == 3
            year_len = len(timestamp[0]) == 4
            month_len = len(timestamp[1]) == 1 or len(timestamp[1]) == 2
            day_len = len(timestamp[2]) == 1 or len(timestamp[2]) == 2

            valid = length and year_len and month_len and day_len

            timestamp = (
                int(timestamp[0]),
                int(timestamp[1]),
                int(timestamp[2]),
            )
            return timestamp if valid else None
        # TODO: !!!
        except:
            return False

    @classmethod
    def custom_query(cls, queryset, created, updated):
        if created:
            valid = cls.validate_timestamp(created)
            if valid:
                queryset = queryset.filter(
                    created_at__year=valid[0],
                    created_at__month=valid[1],
                    created_at__day=valid[2],
                )
        if updated:
            valid = cls.validate_timestamp(updated)
            if valid:
                queryset = queryset.filter(
                    updated_at__year=valid[0],
                    updated_at__month=valid[1],
                    updated_at__day=valid[2],
                )
        return queryset


class AlbumList(generics.ListCreateAPIView, Mixins):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistList(generics.ListCreateAPIView, Mixins):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SoundcodeList(generics.ListCreateAPIView, Mixins):
    serializer_class = SoundcodeSerializer

    def get_queryset(self):
        queryset = Soundcode.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class SoundcodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soundcode.objects.all()
    serializer_class = SoundcodeSerializer


class SongList(generics.ListCreateAPIView, Mixins):
    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
