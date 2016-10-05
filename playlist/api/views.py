from rest_framework import generics

from playlist.models import Artist, Category, Genre, Track
from playlist.api.serializers import (ArtistSerializer, CategorySerializer,
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


class CategoryList(generics.ListCreateAPIView, Mixins):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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


class GenreList(generics.ListCreateAPIView, Mixins):
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
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all()
        created = self.request.query_params.get('created')
        updated = self.request.query_params.get('updated')
        return self.custom_query(queryset, created, updated)


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
