# -*- coding: utf-8 -*-
import os

from django.db import models


def upload_to(instance, filename):
    return os.path.join('covers', filename)


class Album(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to=upload_to, null=True, blank=True)
    published_at = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ('title',)

    def __str__(self):
        return str(self.title)


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name.encode('utf8')


class Category(models.Model):
    category_name = models.CharField(max_length=30, default='default')
    category_code = models.CharField(max_length=1, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('category_name',)

    def __str__(self):
        return self.category_code


class Genre(models.Model):
    genre_name = models.CharField(max_length=30, unique=True)
    genre_code = models.CharField(max_length=1, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('genre_name',)

    def __str__(self):
        return self.genre_code


class Track(models.Model):
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
    category = models.ForeignKey('Category')
    album = models.ForeignKey('Album')
    title = models.CharField(max_length=50)
    artists = models.ManyToManyField('Artist', related_name='artists')
    genres = models.ManyToManyField(Genre)
    mood = models.IntegerField(choices=MOOD, default=1)
    energy = models.IntegerField(choices=ENERGY, default=1)
    tempo = models.CharField(max_length=2, choices=TEMPO_LIST, default='SS')
    related_artists = models.ManyToManyField('Artist', blank=True, related_name='related_artists')
    related_tracks = models.ManyToManyField('Track', blank=True)
    file = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Track'
        verbose_name_plural = 'Tracks'

    def __str__(self):
        return self.song_id
