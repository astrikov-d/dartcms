# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-29 05:15
from __future__ import unicode_literals

import dartcms.utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_homepage_security'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='after_content',
            field=dartcms.utils.fields.RteField(blank=True, default='', verbose_name='After Content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='before_content',
            field=dartcms.utils.fields.RteField(blank=True, default='', verbose_name='Before Content'),
        ),
        migrations.AlterField(
            model_name='page',
            name='menu_name',
            field=models.CharField(default='', max_length=255, verbose_name='Menu name'),
        ),
        migrations.AlterField(
            model_name='page',
            name='redirect_url',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='URL for Redirect'),
        ),
        migrations.AlterField(
            model_name='page',
            name='security_type',
            field=models.CharField(choices=[('DEFAULT', 'Editable for all users'), ('BY_PARENT', 'Based on the parent page'), ('GROUPS_ONLY', 'Editable for specific groups')], default='BY_PARENT', max_length=16, verbose_name='Security type'),
        ),
        migrations.AlterField(
            model_name='page',
            name='seo_description',
            field=models.TextField(blank=True, default='', verbose_name='Description (meta description)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='seo_keywords',
            field=models.TextField(blank=True, default='', verbose_name='Keywords (meta keywords)'),
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, default='', verbose_name='URL'),
        ),
    ]