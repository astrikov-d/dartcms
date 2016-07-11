# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-06 06:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_insert_pagemodules'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagemodule',
            name='related_model',
            field=models.CharField(default=None, max_length=32, null=True, verbose_name='Related Model'),
        ),
        migrations.AlterField(
            model_name='page',
            name='ad_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages_page_related', to='ads.AdSection', verbose_name='Ads'),
        ),
    ]