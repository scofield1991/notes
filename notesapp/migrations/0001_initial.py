# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note_name', models.CharField(max_length=200)),
                ('note_body', models.TextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 8, 17, 6, 43, 36, 773972, tzinfo=utc), editable=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('birthday', models.DateField()),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(regex='^[0-9]{3}-? ?[0-9]{7}$', message="Phone number must be entered in the format: '999-9999999'.")])),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
