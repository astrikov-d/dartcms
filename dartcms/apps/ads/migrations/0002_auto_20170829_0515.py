# Generated by Django 1.10.4 on 2017-08-29 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='bg',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Background Color'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='code',
            field=models.TextField(blank=True, default='', verbose_name='Embed Code'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='link',
            field=models.URLField(blank=True, default='', verbose_name='Ad Link'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='b/%Y/%m/%d', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.TextField(blank=True, default='', verbose_name='Ad Text'),
        ),
    ]
