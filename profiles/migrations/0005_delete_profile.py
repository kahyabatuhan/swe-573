# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20170218_0821'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
