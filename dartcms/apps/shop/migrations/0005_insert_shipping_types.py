# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _

records = [
    dict(sort=1, slug='courier', name=_('Courier')),
    dict(sort=2, slug='mail', name=_('Mail')),
    dict(sort=3, slug='delivery_service', name=_('Delivery service'))
]


def insert(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    model = apps.get_model('shop', 'OrderShippingType')
    for record in records:
        model.objects.create(**record)

    translation.deactivate()


def delete(apps, schema):
    model = apps.get_model('shop', 'OrderShippingType')
    for record in records:
        model.objects.get(slug=record['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0004_insert_payment_types'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]
