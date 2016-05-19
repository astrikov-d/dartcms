# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone


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

    @property
    def clicks_count(self):
        return self.click_set.all().count()

    @property
    def clicks_count_uniq(self):
        return len(
            self.click_set.all().order_by('ip_address', 'user_agent').values('ip_address', 'user_agent').annotate(
                cnt=models.Count('id')))

    @property
    def ctr(self):
        if self.views > 0:
            return "%.2f" % ((float(self.clicks_count) / float(self.views)) * 100)
        return 0

    date_from = models.DateTimeField(default=timezone.now, verbose_name=_(u'Start Date'))
    date_to = models.DateTimeField(default=timezone.now, verbose_name=_(u'End Date'))
    name = models.CharField(max_length=255, verbose_name=_(u'Name'))
    title = models.TextField(default='', blank=True, verbose_name=_(u'Ad Text'))
    link = models.URLField(default='', blank=True, verbose_name=_(u'Ad Link'))
    code = models.TextField(default='', blank=True, verbose_name=_(u'Embed Code'))
    bg = models.CharField(default='', blank=True, max_length=255, verbose_name=_(u'Background Color'))
    place = models.ForeignKey(AdvPlace, verbose_name=_(u'Ad Place'))
    views = models.IntegerField(default=0, verbose_name=_(u"Views"))
    section = models.ManyToManyField(AdvSection, verbose_name=_(u'Section'))
    picture = models.FileField(upload_to="b/%Y/%m/%d", null=True, blank=True, verbose_name=_(u'Picture'))
    is_enabled = models.BooleanField(default=True, verbose_name=_(u'Is Enabled'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Click(models.Model):
    class Meta:
        verbose_name = _(u"click")
        verbose_name_plural = _(u"clicks")
        ordering = ['-date_created']

    ad = models.ForeignKey(Adv, verbose_name=_(u"Advertisement"), on_delete=models.SET_NULL, null=True, blank=True)
    referer = models.CharField(max_length=255, verbose_name=_(u"Referrer"))
    url = models.URLField(verbose_name=u"URL")
    ip_address = models.IPAddressField(null=True, blank=True, verbose_name=u"IP")
    user_agent = models.CharField(max_length=512, verbose_name=u"User-Agent")
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Click %s - %s" % (self.referer, self.url)