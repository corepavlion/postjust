# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150208_2225'),
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
                ('date', models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 27, 324225, tzinfo=utc), verbose_name=b'Publised Date')),
                ('categories', models.ManyToManyField(to='blog.BlogCategory', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 27, 321601, tzinfo=utc), verbose_name=b'Published Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(unique=True, verbose_name=b'Slug Url'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='title',
            field=models.CharField(max_length=250, verbose_name=b'Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 28, 15, 10, 27, 322606, tzinfo=utc), verbose_name=b'Publised Date'),
            preserve_default=True,
        ),
    ]
