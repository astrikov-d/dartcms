# Generated by Django 1.9.6 on 2016-07-05 05:21
from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _

PAGE_MODULES = [
    {'slug': 'feeds', 'name': _('Feeds')},
    {'slug': 'contacts', 'name': _('Contacts')},
    {'slug': 'shop', 'name': _('Shop')},
    {'slug': 'page', 'name': _('Static Page')},
]


def insert_pagemodules(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    PageModule = apps.get_model('pages', 'PageModule')

    for m in PAGE_MODULES:
        PageModule.objects.create(**m)

    translation.deactivate()


def drop_pagemodules(apps, schema):
    PageModule = apps.get_model('pages', 'PageModule')

    for m in PAGE_MODULES:
        PageModule.objects.filter(slug=m['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0002_related_models'),
    ]

    operations = [
        migrations.RunPython(insert_pagemodules, drop_pagemodules)
    ]
