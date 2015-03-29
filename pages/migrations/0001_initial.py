# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
                ('published', models.BooleanField(default=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 29, 21, 4, 19, 98282, tzinfo=utc), verbose_name=b'Publised Date')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
