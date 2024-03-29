# Generated by Django 3.2.8 on 2021-10-08 19:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSUser',
            fields=[
            ],
            options={
                'verbose_name': 'CMS User',
                'verbose_name_plural': 'CMS Users',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Group name')),
                ('users', models.ManyToManyField(related_name='user_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User group',
                'verbose_name_plural': 'User groups',
                'ordering': ['name'],
            },
        ),
    ]
