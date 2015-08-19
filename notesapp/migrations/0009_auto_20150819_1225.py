# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0008_auto_20150819_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='txtcolor',
            new_name='text',
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 12, 25, 8, 579538, tzinfo=utc), editable=False),
        ),
    ]
