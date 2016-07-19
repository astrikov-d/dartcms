# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from dartcms import get_model

model = get_model('shop', 'OrderPaymentType')

records = [
    dict(sort=1, slug='cash', name='Cash'),
    dict(sort=2, slug='cashless', name='Cashless'),
    dict(sort=3, slug='card', name='Credit card')
]


def insert(apps, schema):
    for record in records:
        model.objects.create(**record)


def delete(apps, schema):
    for record in records:
        model.objects.get(slug=record['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0003_auto_add_order_models'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]
