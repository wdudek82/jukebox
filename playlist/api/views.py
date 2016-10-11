from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics

from playlist.models import Album, Artist, Category, Genre, Track
from playlist.api.serializers import (AlbumSerializer, ArtistSerializer, CategorySerializer,
                                      GenreSerializer, TrackSerializer)


class Mixins:
    @classmethod
    def validate_timestamp(cls, timestamp):
        try:
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
        except:
            return None

    @classmethod
    def custom_query(cls, queryset, created, updated):
        if created:
            valid = cls.validate_timestamp(created)
            if valid:
                queryset = queryset.filter(
                    created_at__year__gte=valid[0],
                    created_at__month__gte=valid[1],
                    created_at__day__gte=valid[2],
                )
        elif updated:
            valid = cls.validate_timestamp(updated)
            if valid:
                queryset = queryset.filter(
                    updated_at__year__gte=valid[0],
                    updated_at__month__gte=valid[1],
                    updated_at__day__gte=valid[2],
                )
        return queryset


class CategoryList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AlbumList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = AlbumSerializer

    def get_queryset(self):
        queryset = Album.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class ArtistList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class GenreList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = GenreSerializer

    def get_queryset(self):
        queryset = Genre.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TrackList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all()

        album_id= self.request.query_params.get('album_id')
        if album_id:
            queryset = queryset.filter(album_id=album_id)

        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

