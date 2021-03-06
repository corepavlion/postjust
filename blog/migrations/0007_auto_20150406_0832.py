# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150406_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 8, 32, 0, 895113, tzinfo=utc), verbose_name=b'Published Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 8, 32, 0, 895993, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
    ]
