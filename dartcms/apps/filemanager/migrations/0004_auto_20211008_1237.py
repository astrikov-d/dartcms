# Generated by Django 3.2.8 on 2021-10-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0003_auto_20170829_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='folder',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
