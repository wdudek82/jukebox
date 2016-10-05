import os
from django.contrib import admin
from .models import Album, Artist, Category, Genre, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'get_cover_image', 'published_at', 'created_at', 'updated_at')
    list_display_links = ('title',)
    list_editable = ('description',)
    search_fields = ('title',)

    def get_cover_image(self, instance):
        cover_image = instance.cover_image
        cover_on_disk = os.path.exists(cover_image.path)
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            cover_image.url) if cover_image and cover_on_disk else '-'
    get_cover_image.short_description = 'Cover Image'
    get_cover_image.allow_tags = True


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = ('name', 'created_at', 'updated_at')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_code')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre_name', 'genre_code', 'created_at', 'updated_at')


class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_id', 'category', 'title', 'get_artists', 'get_album', 'get_album_cover_image',
                    'get_genres', 'get_related_artists', 'get_related_tracks', 'mood', 'energy', 'tempo',
                    'file', 'created_at', 'updated_at')
    list_display_links = ('song_id',)
    list_filter = ('category__category_code', 'title', 'artists__name', 'album', 'genres__genre_name',
                   'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    search_fields = ('title', 'artists__name', 'album__title')
    filter_horizontal = ('artists', 'genres', 'related_tracks')

    def get_album(self, instance):
        album = instance.album.title
        return album if album != instance.song_id else '-'
    get_album.short_description = 'Album'

    def get_album_cover_image(self, instance):
        cover_image = instance.album.cover_image
        cover_on_disk = os.path.exists(cover_image.path)
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            cover_image.url) if cover_image and cover_on_disk else '-'
    get_album_cover_image.short_description = 'Cover Image'
    get_album_cover_image.allow_tags = True

    def get_artists(self, instance):
        artists = ', '.join([artist.name for artist in instance.artists.all()])
        return artists
    get_artists.short_description = 'Artists'

    def get_genres(self, instance):
        return ', '.join([genre.genre_name for genre in instance.genres.all()])
    get_genres.short_description = 'Genres'

    def get_related_artists(self, instance):
        artists = ', '.join([artist.name for artist in instance.related_artists.all()])
        return artists or '-'
    get_related_artists.short_description = 'Related Artists'

    def get_related_tracks(self, instance):
        related_tracks = Track.objects.filter(
            category=instance.category,
            tempo=instance.tempo) \
                .exclude(id=instance.id) \
                .values('song_id')
        results = (related_tracks.filter(mood=instance.mood, energy=instance.energy) or
                   related_tracks.filter(energy=instance.energy) or
                   related_tracks)

        tracks = ', '.join(
            [track['song_id'] for track in results]
        )
        return tracks or '-'
    get_related_tracks.short_description = 'Related Tracks'


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Track, TrackAdmin)
