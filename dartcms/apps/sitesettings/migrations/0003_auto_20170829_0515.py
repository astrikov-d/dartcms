# Generated by Django 1.10.4 on 2017-08-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0002_insert_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(default='', verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='file_value',
            field=models.FileField(blank=True, null=True, upload_to='vars', verbose_name='Value for file'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='options',
            field=models.TextField(blank=True, default='', verbose_name='Options for select type (use ";" as separator)'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='text_value',
            field=models.TextField(blank=True, default='', verbose_name='Value for text type'),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='type',
            field=models.CharField(blank=True, choices=[('text', 'String'), ('textarea', 'Text'), ('rich', 'Rich Editor'), ('select', 'Select'), ('date', 'Date'), ('file', 'File')], default='text', max_length=10, verbose_name='Type'),
        ),
    ]
