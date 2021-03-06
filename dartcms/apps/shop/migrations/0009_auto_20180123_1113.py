# Generated by Django 2.0.1 on 2018-01-23 11:13

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20170829_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='manufacturer_products', to='shop.ProductManufacturer', verbose_name='Manufacturer'),
        ),
        migrations.AlterField(
            model_name='product',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.ProductSection', verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='productsection',
            name='catalog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='shop.ProductCatalog', verbose_name='Product catalog'),
        ),
        migrations.AlterField(
            model_name='productsection',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='shop.ProductSection', verbose_name='Parent Section'),
        ),
    ]
