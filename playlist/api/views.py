from datetime import datetime
import pytz

from django.db.models import Q

from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework import generics

from playlist.models import Album, Artist, Category, Genre, Track
from playlist.api.serializers import (AlbumSerializer, ArtistSerializer, CategorySerializer,
                                      GenreSerializer, TrackSerializer)


class Mixins:
    @classmethod
    def convert_timestamp(cls, timestamp):
        try:
            timestamp = datetime.fromtimestamp(int(timestamp))
            aware_timestamp = pytz.timezone('Europe/Warsaw').localize(timestamp)

        except ValueError as e:
            print(e)
            aware_timestamp = None

        return aware_timestamp


class CategoryList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        created = self.request.query_params.get('created')
        if created:
            queryset = queryset.filter(created_at__gte=self.convert_timestamp(created))

        updated = self.request.query_params.get('updated')
        if updated:
            queryset = queryset.filter(updated_at__gte=self.convert_timestamp(updated))

        return queryset


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
        if created:
            queryset = queryset.filter(created_at__gte=self.convert_timestamp(created))

        updated = self.request.query_params.get('updated')
        if updated:
            queryset = queryset.filter(updated_at__gte=self.convert_timestamp(updated))

        return queryset


class ArtistList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = ArtistSerializer

    def get_queryset(self):
        queryset = Artist.objects.all()
        created = self.request.query_params.get('created')
        if created:
            queryset = queryset.filter(created_at__gte=self.convert_timestamp(created))

        updated = self.request.query_params.get('updated')
        if updated:
            queryset = queryset.filter(updated_at__gte=self.convert_timestamp(updated))

        return queryset


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
        if created:
            queryset = queryset.filter(created_at__gte=self.convert_timestamp(created))

        updated = self.request.query_params.get('updated')
        if updated:
            queryset = queryset.filter(updated_at__gte=self.convert_timestamp(updated))

        return queryset


class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TrackList(generics.ListCreateAPIView, Mixins):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = TrackSerializer

    def get_queryset(self):
        queryset = Track.objects.all()

        album_id = self.request.query_params.get('album_id')
        if album_id:
            queryset = queryset.filter(album_id=album_id)

        artist_id = self.request.query_params.get('artist_id')
        if artist_id:
            queryset = queryset.filter(artists__id=artist_id)

        created = self.request.query_params.get('created')
        if created:
            queryset = queryset.filter(created_at__gte=self.convert_timestamp(created))

        updated = self.request.query_params.get('updated')
        if updated:
            queryset = queryset.filter(updated_at__gte=self.convert_timestamp(updated))

        return queryset


class TrackDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

