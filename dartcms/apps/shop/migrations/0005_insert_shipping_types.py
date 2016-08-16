# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


records = [
    dict(sort=1, slug='courier', name='Courier'),
    dict(sort=2, slug='mail', name='Mail'),
    dict(sort=3, slug='delivery_service', name='Delivery service')
]


def insert(apps, schema):
    model = apps.get_model('shop', 'OrderShippingType')
    for record in records:
        model.objects.create(**record)


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
