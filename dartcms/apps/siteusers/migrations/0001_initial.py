# Generated by Django 3.2.8 on 2021-10-08 19:26

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
            ],
            options={
                'verbose_name': 'Site User',
                'verbose_name_plural': 'Site Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
    ]
