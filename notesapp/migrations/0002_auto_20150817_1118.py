# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 17, 11, 18, 24, 449685, tzinfo=utc), editable=False),
        ),
        migrations.AddField(
            model_name='note',
            name='labels',
            field=models.ManyToManyField(to='notesapp.Label'),
        ),
    ]
