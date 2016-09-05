from django.contrib import admin

from .models import Artist, Album, Soundcode, Song


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_display_links = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'created_at', 'updated_at')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_title', 'cover_tag', 'created_at', 'updated_at')
    list_display_links = ('album_title',)
    list_filter = ('album_title', 'created_at', 'updated_at')
    search_fields = ('album_title', 'cover_tag', 'created_at', 'updated_at')


class SoundcodeAdmin(admin.ModelAdmin):
    list_display = ('genre', 'symbol')


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_id', 'song_url', 'artist_1', 'artist_2', 'song_title', 'album', 'get_album_cover',
                    'get_soundcodes', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    list_display_links = ('song_id',)
    list_filter = ('artist_1', 'artist_2', 'song_title', 'album', 'mood',
                   'energy', 'tempo', 'created_at', 'updated_at')
    search_fields = ('id', 'song_id', 'song_url', 'artist_1', 'artist_2', 'song_title',
                     'album', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    filter_horizontal = ('soundcode',)

    def get_album_cover(self, instance):
        cover = instance.album.cover
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            cover.url) if cover else '-'
    get_album_cover.short_description = 'Album Cover'
    get_album_cover.allow_tags = True

    def get_soundcodes(self, instance):
        return ', '.join([code.genre for code in instance.soundcode.all()])


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Soundcode, SoundcodeAdmin)
admin.site.register(Song, SongAdmin)
