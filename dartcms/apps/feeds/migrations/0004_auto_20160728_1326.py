# Generated by Django 1.9.8 on 2016-07-28 13:26
from __future__ import unicode_literals

import autoslug.fields
import dartcms.utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0003_auto_20160712_1142'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'ordering': ['name'], 'verbose_name': 'Feed', 'verbose_name_plural': 'Feeds'},
        ),
        migrations.AlterModelOptions(
            name='feeditem',
            options={'ordering': ['-date_published'], 'verbose_name': 'Feed item', 'verbose_name_plural': 'Feed items'},
        ),
        migrations.AlterModelOptions(
            name='feedtype',
            options={'verbose_name': 'Feed type', 'verbose_name_plural': 'Feed types'},
        ),
        migrations.AddField(
            model_name='feeditem',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Is Main'),
        ),
        migrations.AddField(
            model_name='feeditem',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from=b'name', unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='full_text',
            field=dartcms.utils.fields.RteField(verbose_name='Full Text'),
        ),
        migrations.AlterField(
            model_name='feeditem',
            name='short_text',
            field=dartcms.utils.fields.RteField(verbose_name='Short Text'),
        ),
    ]
