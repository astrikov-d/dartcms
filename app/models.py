# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import datetime
import string
from pytils.translit import slugify
import watson

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.db.models import F
from django.utils.translation import get_language
from django.conf import settings

from lib.utils.hash import random_string


class CMSModuleGroup(models.Model):
    class Meta:
        verbose_name_plural = _(u"CMS Module Groups")
        verbose_name = _(u"CMS Module Group")
        ordering = ['sort']

    def __unicode__(self):
        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.name
        else:
            return self.name_en

    slug = models.SlugField(unique=True, verbose_name=_(u"Slug"))
    name = models.CharField(max_length=64, verbose_name=_(u"Name (RU)"))
    name_en = models.CharField(max_length=64, verbose_name=_(u"Name (EN)"))
    fa = models.SlugField(verbose_name=_(u"FontAwesome class"))
    sort = models.IntegerField(default=1, verbose_name=_(u"Sort"))
    description = models.TextField(default='', verbose_name=_(u"Description"), blank=True)


class CMSModule(models.Model):
    class Meta:
        verbose_name_plural = _(u"CMS Modules")
        verbose_name = _(u"CMS Module")
        ordering = ['group', 'sort']

    def __unicode__(self):
        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.group.name + " / " + self.name
        else:
            return self.group.name_en + " / " + self.name_en

    group = models.ForeignKey(CMSModuleGroup, to_field='slug', verbose_name=_(u"Group"), related_name="cmsmodules")
    name = models.CharField(max_length=64, verbose_name=_(u"Name (RU)"))
    name_en = models.CharField(max_length=64, verbose_name=_(u"Name (EN)"))
    sort = models.IntegerField(default=1, verbose_name=_(u"Sort"))
    description = models.TextField(default='', verbose_name=_(u"Description"), blank=True)
    slug = models.SlugField(unique=True, verbose_name=_(u"Slug"))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u"Is Enabled"))


class Folder(models.Model):
    class Meta:
        verbose_name = _(u"folder")
        verbose_name_plural = _(u"folders")
        ordering = ['name']
        unique_together = ('name',)

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())


class File(models.Model):
    folder = models.ForeignKey(Folder)
    path = models.FileField(upload_to="uploads/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())


@receiver(pre_delete, sender=File)
def files_delete(sender, instance, **kwargs):
    """
    On file delete, we should also delete the file.
    """
    instance.path.delete(False)


class SiteSettings(models.Model):
    """
    Site Settings
    """
    site_title = models.CharField(
        max_length=255,
        default=u"",
        verbose_name=_(u"Site Name"),
    )
    site_description = models.TextField(
        verbose_name=_(u"Site Description")
    )
    footer_content = models.TextField(default=u"", verbose_name=_(u"Footer Content"))


class AdvPlace(models.Model):
    """
    Place for advertisement.
    """

    class Meta:
        verbose_name = _(u"ad place")
        verbose_name_plural = _(u"ad places")
        ordering = ['name']

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    slug = models.SlugField(unique=True)
    is_enabled = models.BooleanField(default=True, verbose_name=_(u'Is Enabled'))


class AdvSection(models.Model):
    """
    Section for advertisement. For example, homepage, or feeds page.
    """

    class Meta:
        verbose_name = _(u"ad section")
        verbose_name_plural = _(u"ad sections")
        ordering = ['name']

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u'Is Enabled'))


class Adv(models.Model):
    """
    Advertisement settings.
    """

    class Meta:
        verbose_name = _(u"banner")
        verbose_name_plural = _(u"banners")
        ordering = ['name']

    date_from = models.DateTimeField(default=datetime.date.today(), verbose_name=_(u'Start Date'))
    date_to = models.DateTimeField(
        default=datetime.date.today() + datetime.timedelta(days=30),
        verbose_name=_(u'End Date'))
    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    title = models.TextField(default='', blank=True, verbose_name=_(u'Ad Text'))
    link = models.URLField(default='', blank=True, verbose_name=_(u'Ad Link'))
    code = models.TextField(default='', blank=True, verbose_name=_(u'Embed Code'))
    bg = models.CharField(default='', blank=True, max_length=255, verbose_name=_(u'Background Color'))
    place = models.ForeignKey(AdvPlace, verbose_name=_(u'Ad Place'))
    section = models.ManyToManyField(AdvSection, verbose_name=_(u'Section'))
    picture = models.FileField(upload_to="b/%Y/%m/%d", null=True, blank=True, verbose_name=_(u'Picture'))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u'Is Enabled'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)


class PageModule(models.Model):
    """
    Page module. I.e. feeds, homepage, catalog etc.
    """

    class Meta:
        ordering = ['id']
        verbose_name_plural = _(u"Modules")
        verbose_name = _(u"Module")

    def __unicode__(self):
        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.name
        else:
            return self.name_en

    slug = models.SlugField(unique=True, verbose_name=_(u"Slug"))
    name = models.CharField(max_length=64, verbose_name=_(u"Name (RU)"))
    name_en = models.CharField(max_length=64, verbose_name=_(u"Name (EN)"))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u"Is Enabled"))


class Page(models.Model):
    """
    Page class.
    """

    class Meta:
        ordering = ['sort']
        verbose_name = _(u"page")
        verbose_name_plural = _(u"pages")
        unique_together = ['module', 'slug']

    def __unicode__(self):
        page = self
        parent = page.parent
        page_names = [page.title]
        while parent:
            page_names.append(parent.title)
            parent = parent.parent
        return string.join(reversed(page_names), " / ")

    parent = models.ForeignKey("self", null=True, related_name='children', verbose_name=_(u"Parent Page"))
    title = models.CharField(max_length=255, verbose_name=_(u'Title'), help_text=_(u'Shows inside the <title/> tag'))
    header = models.CharField(max_length=255, verbose_name=_(u'Page Header'))
    menu_name = models.CharField(max_length=255, default='', verbose_name=_(u'Menu name'))
    menu_url = models.CharField(max_length=255, blank=True, default='', verbose_name=_(u'URL for Redirect'))
    slug = models.SlugField(default='', verbose_name=_(u'URL'))
    url = models.CharField(max_length=512)
    sort = models.IntegerField(default=1)
    module = models.ForeignKey(PageModule, verbose_name=_(u"Module"))
    module_params = models.CharField(max_length=128, blank=True, null=True, default=None,
                                     verbose_name=_(u'Module parameters'))
    before_content = models.TextField(default='', blank=True, verbose_name=_(u'Before Content'))
    after_content = models.TextField(default='', blank=True, verbose_name=_(u'After Content'))
    date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now)
    date_changed = models.DateTimeField(auto_now=True, default=datetime.datetime.now)
    seo_keywords = models.TextField(default='', blank=True, verbose_name=_(u'Keywords (meta keywords)'))
    seo_description = models.TextField(default='', blank=True, verbose_name=_(u'Description (meta description)'))
    adv_section = models.ForeignKey(AdvSection, verbose_name=_(u'Ads'))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u'Is Enabled'))
    is_in_menu = models.BooleanField(default=True, verbose_name=_(u'Show in Menu'))
    is_locked = models.BooleanField(default=False, verbose_name=_(u'Only for Authorized Users'))

    def get_menu_url(self):
        if self.menu_url:
            return self.menu_url

        url = self.url

        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            prefix = ''
        else:
            prefix = '/' + lang

        if self.menu_url != '':
            return prefix + self.menu_url
        return prefix + url

    def delete(self, using=None):
        Page.objects.filter(parent=self.parent, sort__gt=self.sort).update(sort=F('sort') - 1)
        super(Page, self).delete(using=None)

    def get_page_url(self):

        if self.module.slug == 'pagemap':
            return u"/page/%s/" % self.slug
        if self.module.slug == 'feeds':
            return u"/feeds/%s/" % self.slug
        if self.module.slug == 'feedback':
            return u"/feedback/%s/" % self.slug

        return u"/%s/" % self.module.slug

    def save(self, *args, **kwargs):

        self.url = self.get_page_url()

        # Form page sort
        current_level_pages = Page.objects.filter(parent=self.parent)

        if not current_level_pages:
            self.sort = 1

        if not self.id or self.sort == 0:
            from django.db.models import Max

            max_sort = current_level_pages.aggregate(Max('sort'))
            if max_sort['sort__max']:
                self.sort = max_sort['sort__max'] + 1
            else:
                self.sort = 1
        else:
            page_cache = Page.objects.get(pk=self.id)

            if page_cache.parent == self.parent:
                if int(page_cache.sort) < int(self.sort):
                    self.sort -= 1
                    current_level_pages.filter(sort__gt=page_cache.sort, sort__lte=self.sort).update(sort=F('sort') - 1)
                else:
                    current_level_pages.filter(sort__gte=self.sort, sort__lt=page_cache.sort).update(sort=F('sort') + 1)
            else:
                current_level_pages.filter(sort__gte=self.sort).update(sort=F('sort') + 1)
                Page.objects.filter(parent=page_cache.parent, sort__gt=page_cache.sort).update(sort=F('sort') - 1)

        super(Page, self).save(*args, **kwargs)

        childes = self.children.all()
        if childes:
            for child in childes:
                child.save()


class FeedType(models.Model):
    """
    Feed type. I.e. `articles` or `news`
    """
    class Meta:
        verbose_name = _(u"feed type")
        verbose_name_plural = _(u"feed types")

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"Slug"))


class Feed(models.Model):
    class Meta:
        verbose_name = _(u"feed category")
        verbose_name_plural = _(u"feed categories")
        ordering = ['name']
        unique_together = ['type', 'slug']

    def __unicode__(self):
        return self.name

    type = models.ForeignKey(FeedType, verbose_name=_(u"Type"), related_name="feeds")
    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"URL"))


class FeedItem(models.Model):
    class Meta:
        verbose_name = _(u"feed item")
        verbose_name_plural = _(u"feed items")
        ordering = ['-date_published']

    @property
    def search_content_type(self):
        return self.feed.type.slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        while True:
            try:
                FeedItem.objects.get(slug=self.slug)
                self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
            except FeedItem.DoesNotExist:
                break
        super(FeedItem, self).save()

    feed = models.ForeignKey(Feed, verbose_name=_(u"Feed"))
    name = models.CharField(max_length=1024, verbose_name=_(u"Title"))
    slug = models.SlugField(unique=True, verbose_name=_(u"Slug"))
    short_text = models.TextField(verbose_name=_(u"Short Text"))
    full_text = models.TextField(verbose_name=_(u"Full Text"))
    picture = models.ImageField(verbose_name=_(u"Picture"), upload_to="feeds/%Y/%m/%d")
    seo_keywords = models.TextField(
        verbose_name=_(u"Keywords"),
        help_text=_(u"Don't use more than 255 symbols"),
        blank=True
    )
    seo_description = models.TextField(
        verbose_name=_(u"Description"),
        help_text=_(u"Don't use more than 1024 symbols"),
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_(u"Date of Publication"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


watson.register(FeedItem)


class FeedbackType(models.Model):
    """
    Feedback type. I.e. `faq` or `feedback` or `contact`
    """
    class Meta:
        verbose_name = _(u"feedback type")
        verbose_name_plural = _(u"feedback types")
        ordering = ['name']

    @property
    def messages_count(self):
        return self.messages.all().count()

    @property
    def last_message_date(self):
        return self.messages.last().date_created

    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"Slug"))


class FeedbackMessage(models.Model):
    class Meta:
        verbose_name = _(u"feedback message")
        verbose_name_plural = _(u"feedback messages")
        ordering = ['-date_created']

    def __unicode__(self):
        return "%s / %s" % (self.feedback_type.name, self.author)

    feedback_type = models.ForeignKey(FeedbackType, verbose_name=_(u"Type"), related_name='messages')
    author = models.CharField(max_length=255, verbose_name=_(u"Author"))
    email = models.EmailField(verbose_name=_(u"Contact Email"), null=True, blank=True)
    message = models.TextField(verbose_name=_(u"Message"))
    answer = models.TextField(verbose_name=_(u"Answer"))
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_(u"Date of Publication"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))