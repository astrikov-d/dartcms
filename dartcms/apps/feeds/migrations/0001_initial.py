# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='Title')),
                ('short_text', models.TextField(verbose_name='Short Text')),
                ('full_text', models.TextField(verbose_name='Full Text')),
                ('picture', models.ImageField(upload_to=b'feeds/%Y/%m/%d', verbose_name='Picture')),
                ('seo_keywords', models.TextField(blank=True, help_text='Do not use more than 255 symbols', verbose_name='Keywords')),
                ('seo_description', models.TextField(blank=True, help_text='Do not use more than 1024 symbols', verbose_name='Description')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Publication')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.Feed', verbose_name='Feed')),
            ],
            options={
                'ordering': ['-date_published'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='feeds.FeedType', verbose_name='Type'),
        ),
        migrations.AlterUniqueTogether(
            name='feed',
            unique_together=set([('type', 'slug')]),
        ),
    ]
