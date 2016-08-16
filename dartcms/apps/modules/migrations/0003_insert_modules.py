# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations
from django.utils.translation import gettext_lazy as _
from django.utils import translation


def insert_modules(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    ModuleGroup = apps.get_model('modules', 'ModuleGroup')
    Module = apps.get_model('modules', 'Module')

    module = {
        'sort': 2,
        'is_enabled': True,
        'name': _('Site settings'),
        'slug': 'sitesettings',
        'description': '',
        'group': ModuleGroup.objects.get(slug='admin')
    }

    Module.objects.create(**module)

    translation.deactivate()

def delete_modules(apps, schema):
    Module = apps.get_model('modules', 'Module')

    Module.objects.get(slug='sitesettings').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('modules', '0002_insert_modules'),
    ]

    operations = [
        migrations.RunPython(insert_modules, delete_modules)
    ]
