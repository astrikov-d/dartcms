# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations


def insert_modules(apps, schema):
    ModuleGroup = apps.get_model('modules', 'ModuleGroup')
    Module = apps.get_model('modules', 'Module')

    module = {
        'sort': 4,
        'is_enabled': True,
        'name': 'Orders',
        'slug': 'shop-orders',
        'description': '',
        'group': ModuleGroup.objects.get(slug='shop')
    }

    Module.objects.create(**module)


def delete_modules(apps, schema):
    Module = apps.get_model('modules', 'Module')

    Module.objects.get(slug='shop-order').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0006_insert_shop_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
