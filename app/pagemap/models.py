__author__ = 'astrikovd'

import datetime
import string

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db.models import F
from django.utils.translation import get_language
from django.conf import settings

from app.adv.models import AdvSection


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
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)
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