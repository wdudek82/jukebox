from rest_framework import generics

from playlist.models import Album, Artist, Soundcode, Song
from playlist.api.serializers import (AlbumSerializer, ArtistSerializer,
                                      SoundcodeSerializer, SongSerializer)


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SoundcodeList(generics.ListCreateAPIView):
    queryset = Soundcode.objects.all()
    serializer_class = SoundcodeSerializer


class SoundcodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Soundcode.objects.all()
    serializer_class = SoundcodeSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
