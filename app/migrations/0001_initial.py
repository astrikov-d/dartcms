# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_from', models.DateTimeField(default=datetime.date(2015, 1, 20), verbose_name='Start Date')),
                ('date_to', models.DateTimeField(default=datetime.date(2015, 2, 19), verbose_name='End Date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('title', models.TextField(default=b'', verbose_name='Ad Text', blank=True)),
                ('link', models.URLField(default=b'', verbose_name='Ad Link', blank=True)),
                ('code', models.TextField(default=b'', verbose_name='Embed Code', blank=True)),
                ('bg', models.CharField(default=b'', max_length=255, verbose_name='Background Color', blank=True)),
                ('picture', models.FileField(upload_to=b'b/%Y/%m/%d', null=True, verbose_name='Picture', blank=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_changed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'ad place',
                'verbose_name_plural': 'ad places',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AdvSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'ad section',
                'verbose_name_plural': 'ad sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CMSModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('sort', models.IntegerField(default=1, verbose_name='Sort')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['group', 'sort'],
                'verbose_name': 'CMS Module',
                'verbose_name_plural': 'CMS Modules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CMSModuleGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('fa', models.SlugField(verbose_name='FontAwesome class')),
                ('sort', models.IntegerField(default=1, verbose_name='Sort')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'CMS Module Group',
                'verbose_name_plural': 'CMS Module Groups',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='URL')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'feed category',
                'verbose_name_plural': 'feed categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=255, verbose_name='Author')),
                ('email', models.EmailField(max_length=75, null=True, verbose_name='Contact Email', blank=True)),
                ('message', models.TextField(verbose_name='Message')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Publication')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'feedback message',
                'verbose_name_plural': 'feedback messages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'feedback type',
                'verbose_name_plural': 'feedback types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('short_text', models.TextField(verbose_name='Short Text')),
                ('full_text', models.TextField(verbose_name='Full Text')),
                ('picture', models.ImageField(upload_to=b'feeds/%Y/%m/%d', verbose_name='Picture')),
                ('seo_keywords', models.TextField(help_text="Don't use more than 255 symbols", verbose_name='Keywords', blank=True)),
                ('seo_description', models.TextField(help_text="Don't use more than 1024 symbols", verbose_name='Description', blank=True)),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date of Publication')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('feed', models.ForeignKey(verbose_name='Feed', to='app.Feed')),
            ],
            options={
                'ordering': ['-date_published'],
                'verbose_name': 'feed item',
                'verbose_name_plural': 'feed items',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'feed type',
                'verbose_name_plural': 'feed types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FileField(upload_to=b'uploads/%Y/%m/%d')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 1, 20, 13, 19, 3, 176075), auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2015, 1, 20, 13, 19, 3, 175713), auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'folder',
                'verbose_name_plural': 'folders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text='Shows inside the <title/> tag', max_length=255, verbose_name='Title')),
                ('header', models.CharField(max_length=255, verbose_name='Page Header')),
                ('menu_name', models.CharField(default=b'', max_length=255, verbose_name='Menu name')),
                ('menu_url', models.CharField(default=b'', max_length=255, verbose_name='URL for Redirect', blank=True)),
                ('slug', models.SlugField(default=b'', verbose_name='URL')),
                ('url', models.CharField(max_length=512)),
                ('sort', models.IntegerField(default=1)),
                ('module_params', models.CharField(default=None, max_length=128, null=True, verbose_name='Module parameters', blank=True)),
                ('before_content', models.TextField(default=b'', verbose_name='Before Content', blank=True)),
                ('after_content', models.TextField(default=b'', verbose_name='After Content', blank=True)),
                ('date_created', models.DateTimeField(default=datetime.datetime.now, auto_now_add=True)),
                ('date_changed', models.DateTimeField(default=datetime.datetime.now, auto_now=True)),
                ('seo_keywords', models.TextField(default=b'', verbose_name='Keywords (meta keywords)', blank=True)),
                ('seo_description', models.TextField(default=b'', verbose_name='Description (meta description)', blank=True)),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
                ('is_in_menu', models.BooleanField(default=True, verbose_name='Show in Menu')),
                ('is_locked', models.BooleanField(default=False, verbose_name='Only for Authorized Users')),
                ('adv_section', models.ForeignKey(verbose_name='Ads', to='app.AdvSection')),
            ],
            options={
                'ordering': ['sort'],
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageModule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=64, verbose_name='Name (RU)')),
                ('name_en', models.CharField(max_length=64, verbose_name='Name (EN)')),
                ('is_enabled', models.BooleanField(default=True, verbose_name='Is Enabled')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Module',
                'verbose_name_plural': 'Modules',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('slug', models.SlugField(max_length=1024, verbose_name='Slug')),
                ('code', models.CharField(max_length=1024, null=True, verbose_name='Code', blank=True)),
                ('short_description', models.TextField(null=True, verbose_name='Short description', blank=True)),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('views_count', models.IntegerField(default=0, verbose_name='Views Count')),
                ('price', models.DecimalField(default=0, verbose_name='Price', max_digits=10, decimal_places=2)),
                ('residue', models.IntegerField(default=0, verbose_name='Residue')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('is_special_offer', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('seo_keywords', models.TextField(help_text="Don't use more than 255 symbols", verbose_name='Keywords', blank=True)),
                ('seo_description', models.TextField(help_text="Don't use more than 1024 symbols", verbose_name='Description', blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('slug', models.SlugField(max_length=1024, verbose_name='Slug')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'product category',
                'verbose_name_plural': 'product categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('slug', models.SlugField(max_length=1024, verbose_name='Slug')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=b'shop/%Y/%m/%d', verbose_name='Picture')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('product', models.ForeignKey(related_name='pictures', verbose_name='Product', to='app.Product')),
            ],
            options={
                'ordering': ['-date_created'],
                'verbose_name': 'product picture',
                'verbose_name_plural': 'product pictures',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024, verbose_name='Name')),
                ('slug', models.SlugField(max_length=1024, verbose_name='Slug')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Show on Site')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date of Creation')),
                ('category', models.ForeignKey(related_name='sections', on_delete=django.db.models.deletion.DO_NOTHING, verbose_name='Category', to='app.ProductCategory')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'product section',
                'verbose_name_plural': 'product sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_title', models.CharField(default='', max_length=255, verbose_name='Site Name')),
                ('site_description', models.TextField(verbose_name='Site Description')),
                ('footer_content', models.TextField(default='', verbose_name='Footer Content')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='product',
            name='labels',
            field=models.ManyToManyField(to='app.ProductLabel', null=True, verbose_name='Labels', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='section',
            field=models.ForeignKey(related_name='products', on_delete=django.db.models.deletion.DO_NOTHING, verbose_name='Section', to='app.ProductSection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='module',
            field=models.ForeignKey(verbose_name='Module', to='app.PageModule'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(related_name='children', verbose_name='Parent Page', to='app.Page', null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='page',
            unique_together=set([('module', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='folder',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='file',
            name='folder',
            field=models.ForeignKey(to='app.Folder'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feedbackmessage',
            name='feedback_type',
            field=models.ForeignKey(related_name='messages', verbose_name='Type', to='app.FeedbackType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='feed',
            name='type',
            field=models.ForeignKey(related_name='feeds', verbose_name='Type', to='app.FeedType'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='feed',
            unique_together=set([('type', 'slug')]),
        ),
        migrations.AddField(
            model_name='cmsmodule',
            name='group',
            field=models.ForeignKey(related_name='cmsmodules', verbose_name='Group', to_field=b'slug', to='app.CMSModuleGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adv',
            name='place',
            field=models.ForeignKey(verbose_name='Ad Place', to='app.AdvPlace'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='adv',
            name='section',
            field=models.ManyToManyField(to='app.AdvSection', verbose_name='Section'),
            preserve_default=True,
        ),
    ]
