# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0003_auto_20150817_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='color',
            field=colorful.fields.RGBColorField(default='#123456'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 8, 18, 9, 41, 28, 758452, tzinfo=utc)),
        ),
    ]
