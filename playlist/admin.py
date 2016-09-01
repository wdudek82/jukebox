from django.contrib import admin

from .models import Artist, Soundcode, Song


admin.site.register(Artist)
admin.site.register(Soundcode)
admin.site.register(Song)