# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


records = [
    dict(sort=1, slug='cash', name='Cash'),
    dict(sort=2, slug='cashless', name='Cashless'),
    dict(sort=3, slug='card', name='Credit card')
]


def insert(apps, schema):
    model = apps.get_model('shop', 'OrderPaymentType')
    for record in records:
        model.objects.create(**record)


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
