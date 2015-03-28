# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150328_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 15, 6, 441828, tzinfo=utc), verbose_name=b'Published Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 15, 6, 442698, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='page',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 15, 6, 444227, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
    ]
