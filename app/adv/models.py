__author__ = 'astrikovd'

import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models


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
