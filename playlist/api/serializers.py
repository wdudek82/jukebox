from rest_framework import serializers
from playlist.models import Album, Artist, Soundcode, Song


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'album_title', 'image', 'created_at', 'updated_at')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'image', 'created_at', 'updated_at')


class SoundcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soundcode
        fields = ('id', 'symbol', 'genre', 'image', 'created_at', 'updated_at')


class SongSerializer(serializers.ModelSerializer):
    soundcode = serializers.StringRelatedField(many=True)

    class Meta:
        model = Song
        fields = ('id', 'song_id', 'song_url', 'image', 'song_title', 'album', 'artist_1', 'artist_2',
                  'soundcode', 'related_tracks', 'related_artists', 'mood', 'energy', 'tempo',
                  'created_at', 'updated_at')

