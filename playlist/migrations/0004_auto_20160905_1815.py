# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 18:15
from __future__ import unicode_literals

from django.db import migrations, models
import playlist.models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_auto_20160904_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=playlist.models.upload_to),
        ),
    ]