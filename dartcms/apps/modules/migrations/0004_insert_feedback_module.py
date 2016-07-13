# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations

from dartcms.apps.modules.models import Module, ModuleGroup


def insert_modules(apps, schema):
    module = {
        'sort': 1,
        'is_enabled': True,
        'name': 'Feedback',
        'slug': 'feedback',
        'description': '',
        'group': ModuleGroup.objects.get(slug='service')
    }

    Module.objects.create(**module)


def delete_modules(apps, schema):
    Module.objects.get(slug='feedback').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0003_insert_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
