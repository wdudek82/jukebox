from rest_framework import serializers
from playlist.models import Artist, Category, Genre, Track


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
    artists = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=False)
    genres = serializers.StringRelatedField(many=True)

    class Meta:
        model = Track
        fields = ('id', 'song_id', 'category', 'song_url', 'image', 'song_title', 'artists',
                  'genres', 'related_tracks', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')

