# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.utils import translation
from django.utils.translation import gettext_lazy as _


records = [
    dict(sort=1, slug='cash', name=_('Cash')),
    dict(sort=2, slug='cashless', name=_('Cashless')),
    dict(sort=3, slug='card', name=_('Credit card'))
]


def insert(apps, schema):
    from django.conf import settings
    translation.activate(settings.LANGUAGE_CODE)

    model = apps.get_model('shop', 'OrderPaymentType')
    for record in records:
        model.objects.create(**record)

    translation.deactivate()


def delete(apps, schema):
    model = apps.get_model('shop', 'OrderPaymentType')
    for record in records:
        model.objects.get(slug=record['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0003_auto_add_order_models'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]
