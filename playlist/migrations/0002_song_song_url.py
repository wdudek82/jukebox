# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_url',
            field=models.CharField(default='blablabla', max_length=500),
            preserve_default=False,
        ),
    ]