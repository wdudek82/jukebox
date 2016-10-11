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
    album_id = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())
    artists = serializers.StringRelatedField(many=True)
    category = serializers.StringRelatedField(many=False)
    genres = serializers.StringRelatedField(many=True)
    related_tracks = serializers.SerializerMethodField()

    class Meta:
        model = Track
        fields = ('id', 'song_id', 'category', 'title', 'artists', 'album', 'album_id', 'genres', 'related_tracks',
                  'mood', 'energy', 'tempo', 'file', 'created_at', 'updated_at')

    def get_related_tracks(self, instance):
        related_tracks = Track.objects.filter(
            category=instance.category,
            tempo=instance.tempo) \
                .exclude(id=instance.id) \
                .values('id')
        results = (related_tracks.filter(mood=instance.mood, energy=instance.energy) or
                   related_tracks.filter(energy=instance.energy) or
                   related_tracks)

        tracks = [track['id'] for track in results]
        return tracks
