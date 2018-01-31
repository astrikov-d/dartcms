# Generated by Django 2.0.1 on 2018-01-23 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20170829_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='ad_section',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pages_page_related', to='ads.AdSection', verbose_name='Ads'),
        ),
        migrations.AlterField(
            model_name='page',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages_page_related', to='pages.PageModule', verbose_name='Module'),
        ),
    ]
