# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _


records = [
    dict(sort=1, slug='accepted', name=_('Accepted')),
    dict(sort=2, slug='performed', name=_('Performed')),
    dict(sort=3, slug='awaiting_payment', name=_('Avaiting payment')),
    dict(sort=4, slug='delivered', name=_('Delivered')),
    dict(sort=5, slug='ready', name=_('Ready')),
    dict(sort=6, slug='completed', name=_('Completed')),
    dict(sort=7, slug='canceled', name=_('Canceled'))
]


def insert(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    model = apps.get_model('shop', 'OrderStatus')
    for record in records:
        model.objects.create(**record)

    translation.deactivate()


def delete(apps, schema):
    model = apps.get_model('shop', 'OrderStatus')
    for record in records:
        model.objects.get(slug=record['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0005_insert_shipping_types'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]
