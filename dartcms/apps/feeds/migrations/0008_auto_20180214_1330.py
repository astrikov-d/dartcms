# Generated by Django 2.0.1 on 2018-02-14 13:30

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0007_auto_20180123_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeditem',
            name='picture',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='feeds/%Y/%m/%d', verbose_name='Picture'),
        ),
    ]
