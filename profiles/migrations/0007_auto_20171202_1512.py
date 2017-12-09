# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='score',
            field=models.IntegerField(),
        ),
    ]
