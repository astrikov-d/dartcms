# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from dartcms.apps.modules.models import Module, ModuleGroup

MODULE_GROUPS = [
    {
        'sort': 5,
        'description': '',
        'fa': 'fa-shopping-cart',
        'slug': 'shop',
        'name': 'Shop',
        'modules': [
            {
                'sort': 1,
                'is_enabled': True,
                'name': 'Product catalogs',
                'slug': 'shop-catalog',
                'description': ''
            },
            {
                'sort': 2,
                'is_enabled': True,
                'name': 'Product manufacturers',
                'slug': 'shop-manufactures',
                'description': ''
            },
            {
                'sort': 3,
                'is_enabled': True,
                'name': 'Product labels',
                'slug': 'shop-labels',
                'description': ''
            },
        ]
    },
]


def insert_modules(apps, schema):
    for group in MODULE_GROUPS:
        group_modules = group.pop('modules', [])
        group = ModuleGroup.objects.create(**group)
        for module in group_modules:
            module['group'] = group
            Module.objects.create(**module)


def delete_modules(apps, schema):
    for group in MODULE_GROUPS:
        ModuleGroup.objects.get(slug=group['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0005_insert_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
