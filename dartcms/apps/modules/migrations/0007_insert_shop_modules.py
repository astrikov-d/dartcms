# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations

from dartcms.apps.modules.models import Module, ModuleGroup


def insert_modules(apps, schema):
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
    Module.objects.get(slug='shop-order').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0006_insert_shop_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
