# Generated by Django 1.10.4 on 2016-12-14 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161214_0258'),
        ('pages', '0009_auto_20161130_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='security_type',
            field=models.CharField(choices=[
                (b'DEFAULT', 'Editable for all users'),
                (b'BY_PARENT', 'Based on the parent page'),
                (b'GROUPS_ONLY', 'Editable for specific groups')
            ], default=b'BY_PARENT', max_length=16, verbose_name='Security type'),
        ),
        migrations.AddField(
            model_name='page',
            name='user_groups',
            field=models.ManyToManyField(to='users.UserGroup', verbose_name='User groups'),
        ),
    ]
