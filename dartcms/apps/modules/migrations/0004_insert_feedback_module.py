# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations


def insert_modules(apps, schema):
    ModuleGroup = apps.get_model('modules', 'ModuleGroup')
    Module = apps.get_model('modules', 'Module')

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
    Module = apps.get_model('modules', 'Module')

    Module.objects.get(slug='feedback').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0003_insert_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
