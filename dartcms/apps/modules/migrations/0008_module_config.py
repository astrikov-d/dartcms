# Generated by Django 1.9.7 on 2016-07-29 02:29
from __future__ import unicode_literals

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0007_insert_shop_modules'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='config',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Config'),
        ),
    ]
