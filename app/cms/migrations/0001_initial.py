# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('sort', models.IntegerField(default=1, verbose_name='Sort')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['group', 'sort'],
                'verbose_name': 'CMS Module',
                'verbose_name_plural': 'CMS Modules',
            },
        ),
        migrations.CreateModel(
            name='CMSModuleGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('fa', models.SlugField(verbose_name='FontAwesome class')),
                ('sort', models.IntegerField(default=1, verbose_name='Sort')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'CMS Module Group',
                'verbose_name_plural': 'CMS Module Groups',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FileField(upload_to=b'uploads/%Y/%m/%d')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'folder',
                'verbose_name_plural': 'folders',
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('descr', models.TextField(default=b'')),
                ('type', models.CharField(default='text', max_length=10, blank=True, choices=[('text', 'String'), ('textarea', 'Text'), ('rich', 'Rich Editor'), ('select', 'Select'), ('date', 'Date'), ('file', 'File')])),
                ('text_value', models.TextField(default=b'', blank=True)),
                ('date_value', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('file_value', models.FileField(null=True, upload_to=b'vars', blank=True)),
                ('options', models.TextField(default=b'', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Site setting',
                'verbose_name_plural': 'Site settings',
            },
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(to='cms.Folder'),
        ),
        migrations.AddField(
            model_name='cmsmodule',
            name='group',
            field=models.ForeignKey(related_name='cmsmodules', verbose_name='Group', to_field=b'slug', to='cms.CMSModuleGroup'),
        ),
        migrations.AddField(
            model_name='cmsmodule',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
