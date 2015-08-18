# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0002_auto_20150817_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='permit',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=3, default='N'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 8, 17, 13, 18, 29, 441984, tzinfo=utc)),
        ),
    ]
