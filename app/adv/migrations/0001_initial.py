# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Date')),
                ('date_to', models.DateTimeField(default=django.utils.timezone.now, verbose_name='End Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('title', models.TextField(default=b'', verbose_name='Ad Text', blank=True)),
                ('link', models.URLField(default=b'', verbose_name='Ad Link', blank=True)),
                ('code', models.TextField(default=b'', verbose_name='Embed Code', blank=True)),
                ('bg', models.CharField(default=b'', max_length=255, verbose_name='Background Color', blank=True)),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('picture', models.FileField(upload_to=b'b/%Y/%m/%d', null=True, verbose_name='Picture', blank=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
        migrations.CreateModel(
            name='AdvPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'ad place',
                'verbose_name_plural': 'ad places',
            },
        ),
        migrations.CreateModel(
            name='AdvSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'ad section',
                'verbose_name_plural': 'ad sections',
            },
        ),
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referer', models.CharField(max_length=255, verbose_name='Referrer')),
                ('url', models.URLField(verbose_name='URL')),
                ('ip_address', models.IPAddressField(null=True, verbose_name='IP', blank=True)),
                ('user_agent', models.CharField(max_length=512, verbose_name='User-Agent')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Advertisement', blank=True, to='adv.Adv', null=True)),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'click',
                'verbose_name_plural': 'clicks',
            },
        ),
        migrations.AddField(
            model_name='adv',
            name='place',
            field=models.ForeignKey(verbose_name='Ad Place', to='adv.AdvPlace'),
        ),
        migrations.AddField(
            model_name='adv',
            name='section',
            field=models.ManyToManyField(to='adv.AdvSection', verbose_name='Section'),
        ),
    ]
