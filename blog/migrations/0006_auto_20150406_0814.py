# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150328_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 8, 14, 32, 293161, tzinfo=utc), verbose_name=b'Published Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 6, 8, 14, 32, 294283, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
    ]
