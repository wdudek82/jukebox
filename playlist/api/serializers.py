from rest_framework import serializers
from playlist.models import Album, Artist, Soundcode, Song


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'album_title', 'cover', 'created_at', 'updated_at')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'created_at', 'updated_at')


class SoundcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Soundcode
        fields = ('id', 'symbol', 'genre')


class SongSerializer(serializers.ModelSerializer):
    soundcode = serializers.StringRelatedField(many=True)
    # album = serializers.StringRelatedField(many=False)

    class Meta:
        model = Song
        depth = 1
        fields = ('id', 'song_id', 'song_url', 'song_title', 'album', 'artist_1', 'artist_2',
                  'soundcode', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')

