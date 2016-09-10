# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-10 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0010_artist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='related_artists',
            field=models.ManyToManyField(to='playlist.Artist'),
        ),
        migrations.AddField(
            model_name='song',
            name='related_tracks',
            field=models.ManyToManyField(to='playlist.Song'),
        ),
    ]
