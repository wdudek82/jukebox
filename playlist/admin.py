from django.contrib import admin

from .models import Artist, Album, Soundcode, Song


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'created_at', 'updated_at')
    list_display_links = ('name',)
    search_fields = ('name', 'created_at', 'updated_at')

    def get_image(self, instance):
        image = instance.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            image.url) if image else '-'
    get_image.short_description = 'Image'
    get_image.allow_tags = True


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_title', 'get_image', 'created_at', 'updated_at')
    list_display_links = ('album_title',)
    list_filter = ('album_title', 'created_at', 'updated_at')
    search_fields = ('album_title', 'cover_tag', 'created_at', 'updated_at')

    def get_image(self, instance):
        image = instance.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            image.url) if image else '-'
    get_image.short_description = 'Image'
    get_image.allow_tags = True


class SoundcodeAdmin(admin.ModelAdmin):
    list_display = ('genre', 'symbol', 'get_image', 'created_at', 'updated_at')

    def get_image(self, instance):
        image = instance.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            image.url) if image else '-'
    get_image.short_description = 'Image'
    get_image.allow_tags = True


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'song_id', 'song_url', 'get_image', 'artist_1', 'artist_2', 'song_title', 'album',
                    'get_album_cover', 'get_soundcodes', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    list_display_links = ('song_id',)
    list_filter = ('artist_1', 'artist_2', 'song_title', 'album', 'mood',
                   'energy', 'tempo', 'created_at', 'updated_at')
    search_fields = ('id', 'song_id', 'song_url', 'artist_1', 'artist_2', 'song_title',
                     'album', 'mood', 'energy', 'tempo', 'created_at', 'updated_at')
    filter_horizontal = ('soundcode',)

    def get_image(self, instance):
        image = instance.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            image.url) if image else '-'
    get_image.short_description = 'Image'
    get_image.allow_tags = True

    def get_album_cover(self, instance):
        image = instance.album.image
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            image.url) if image else '-'
    get_album_cover.short_description = 'Album Cover'
    get_album_cover.allow_tags = True

    @staticmethod
    def get_soundcodes(instance):
        return ', '.join([code.genre for code in instance.soundcode.all()])


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Soundcode, SoundcodeAdmin)
admin.site.register(Song, SongAdmin)
