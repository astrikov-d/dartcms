# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations

from dartcms import get_model

model = get_model('shop', 'OrderStatus')

records = [
    dict(sort=1, slug='accepted', name='Accepted'),
    dict(sort=2, slug='performed', name='Performed'),
    dict(sort=3, slug='awaiting_payment', name='Avaiting payment'),
    dict(sort=4, slug='delivered', name='Delivered'),
    dict(sort=5, slug='ready', name='Ready'),
    dict(sort=6, slug='completed', name='Completed'),
    dict(sort=7, slug='canceled', name='Canceled')
]


def insert(apps, schema):
    for record in records:
        model.objects.create(**record)


def delete(apps, schema):
    for record in records:
        model.objects.get(slug=record['slug']).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0005_insert_shipping_types'),
    ]

    operations = [
        migrations.RunPython(insert, delete)
    ]
