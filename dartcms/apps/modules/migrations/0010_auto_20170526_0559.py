# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-26 05:59
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0009_insert_user_group_module'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModulePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('can_insert', models.BooleanField(default=True, verbose_name='Can insert data')),
                ('can_update', models.BooleanField(default=True, verbose_name='Can update data')),
                ('can_delete', models.BooleanField(default=True, verbose_name='Can delete data')),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Module permission',
                'verbose_name_plural': 'Module permissions',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='modulegroup',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='modulepermission',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='module_permissions', to='modules.Module', verbose_name='Module'),
        ),
        migrations.AddField(
            model_name='modulepermission',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_module_permissions', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
