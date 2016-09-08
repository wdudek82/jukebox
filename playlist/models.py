import os
from django.conf import settings
from django.db import models


def upload_to(instance, filename):
    return os.path.join('covers', filename)


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'


class Album(models.Model):
    album_title = models.CharField(max_length=50)  # Add unique after albums addition to import data
    cover = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.album_title

    def cover_tag(self):
        return '<a href="{0}" target="_blank"><img src="{0}" width="200"</a>'.format(
            self.cover.url) if self.cover else '-'
    cover_tag.short_description = 'cover'
    cover_tag.allow_tags = True

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ('album_title',)


class Soundcode(models.Model):
    genre = models.CharField(max_length=30, unique=True)
    symbol = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.symbol

    class Meta:
        verbose_name = 'Soundcode'
        verbose_name_plural = 'Soundcodes'
        ordering = ('genre',)


class Song(models.Model):
    TEMPO_LIST = (
        ('SS', 'ad lib-60'),
        ('SM', '61-81'),
        ('SF', '82-89'),

        ('MS', '90-97'),
        ('MM', '98-106'),
        ('MF', '107-118'),

        ('FS', '119-124'),
        ('FM', '125-130'),
        ('FF', '131-inf.'),
    )

    MOOD = ((num, num) for num in range(1, 6))
    ENERGY = ((num, num) for num in range(1, 6))

    song_id = models.CharField(max_length=15, unique=True)
    song_url = models.CharField(max_length=500)
    artist_1 = models.ForeignKey('playlist.Artist', related_name='artist1')
    artist_2 = models.ForeignKey('playlist.Artist', related_name='artist2', null=True, blank=True)
    song_title = models.CharField(max_length=50)
    album = models.ForeignKey('playlist.Album')
    soundcode = models.ManyToManyField(Soundcode)
    mood = models.IntegerField(choices=MOOD, default=1)
    energy = models.IntegerField(choices=ENERGY, default=1)
    tempo = models.CharField(max_length=2, choices=TEMPO_LIST, default='SS')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.song_id

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'
