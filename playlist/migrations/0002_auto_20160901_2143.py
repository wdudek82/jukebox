# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='sound_code',
            new_name='soundcode',
        ),
        migrations.AddField(
            model_name='song',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='song',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist_2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='artist2', to='playlist.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_id',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='soundcode',
            name='symbol',
            field=models.CharField(max_length=1, unique=True),
        ),
        migrations.AlterField(
            model_name='soundcode',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
