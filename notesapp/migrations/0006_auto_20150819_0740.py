# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0005_auto_20150819_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.ManyToManyField(to='notesapp.Category'),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 7, 40, 43, 670212, tzinfo=utc), editable=False),
        ),
    ]
