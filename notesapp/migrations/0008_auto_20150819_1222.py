# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0007_auto_20150819_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='txtcolor',
            field=colorful.fields.RGBColorField(default='#000000'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 12, 22, 36, 291303, tzinfo=utc), editable=False),
        ),
    ]
