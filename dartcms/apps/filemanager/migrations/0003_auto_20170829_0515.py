# Generated by Django 1.10.4 on 2017-08-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_auto_20160711_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='path',
            field=models.FileField(max_length=300, upload_to='uploads/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='name',
            field=models.CharField(error_messages={'unique': 'Folder with this name is already exists'}, max_length=255, unique=True),
        ),
    ]
