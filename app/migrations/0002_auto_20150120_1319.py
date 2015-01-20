# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsmodule',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 13, 19, 10, 887019), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='folder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 13, 19, 10, 886665), auto_now_add=True),
            preserve_default=True,
        ),
    ]
