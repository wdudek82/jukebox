from rest_framework import serializers
from playlist.models import Album, Artist, Category, Genre, Track


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'title', 'published_at', 'created_at', 'updated_at')


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'created_at', 'updated_at')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_code')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'genre_name', 'genre_code', 'created_at', 'updated_at')


class TrackSerializer(serializers.ModelSerializer):
    album = serializers.StringRelatedField(many=False)
    artists = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=False)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ('id', 'song_id', 'category', 'title', 'artists', 'album', 'genres', 'related_tracks',
                  'mood', 'energy', 'tempo', 'file', 'created_at', 'updated_at')

