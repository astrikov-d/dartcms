# Generated by Django 1.9.7 on 2016-07-11 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_pagemodules_relationships'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
