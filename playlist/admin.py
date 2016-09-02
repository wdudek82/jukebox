from django.contrib import admin

from .models import Artist, Album, Soundcode, Song


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_title', 'cover')
    list_display_links = ('album_title',)


class SoundcodeAdmin(admin.ModelAdmin):
    list_display = ('genre', 'symbol')


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_id', 'song_url', 'artist_1', 'artist_2', 'song_title',
                    'album', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    list_display_links = ('song_id',)


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Soundcode, SoundcodeAdmin)
admin.site.register(Song, SongAdmin)
