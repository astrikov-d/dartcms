# coding: utf-8

from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _


def insert_modules(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    ModuleGroup = apps.get_model('modules', 'ModuleGroup')
    Module = apps.get_model('modules', 'Module')

    module = {
        'sort': 1,
        'is_enabled': True,
        'name': _('Feedback'),
        'slug': 'feedback',
        'description': '',
        'group': ModuleGroup.objects.get(slug='service')
    }

    Module.objects.create(**module)

    translation.deactivate()


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
