# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job',
            field=models.CharField(default=b'Some Default', max_length=120),
        ),
        migrations.AddField(
            model_name='profile',
            name='job2',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default=datetime.datetime(2017, 2, 18, 5, 19, 35, 316000, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default=b'My description', null=True, blank=True),
        ),
    ]
