# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class AdPlace(models.Model):
    class Meta:
        app_label = 'ads'
        verbose_name = _('ad place')
        verbose_name_plural = _('ad places')
        ordering = ['name']

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(unique=True)
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))


@python_2_unicode_compatible
class AdSection(models.Model):
    class Meta:
        app_label = 'ads'
        verbose_name = _('ad section')
        verbose_name_plural = _('ad sections')
        ordering = ['name']

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))


@python_2_unicode_compatible
class AbstractAd(models.Model):
    class Meta:
        app_label = 'ads'
        verbose_name = _('ad')
        verbose_name_plural = _('ads')
        ordering = ['name']
        abstract = True

    date_from = models.DateTimeField(default=timezone.now, verbose_name=_('Start Date'))
    date_to = models.DateTimeField(default=timezone.now, verbose_name=_('End Date'))
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    title = models.TextField(default='', blank=True, verbose_name=_('Ad Text'))
    link = models.URLField(default='', blank=True, verbose_name=_('Ad Link'))
    code = models.TextField(default='', blank=True, verbose_name=_('Embed Code'))
    bg = models.CharField(default='', blank=True, max_length=255, verbose_name=_('Background Color'))
    place = models.ForeignKey('ads.AdPlace', verbose_name=_('Ad Place'),
                              related_name='%(app_label)s_%(class)s_related')
    views = models.IntegerField(default=0, verbose_name=_('Views'))
    section = models.ManyToManyField('ads.AdSection', verbose_name=_('Section'),
                                     related_name='%(app_label)s_%(class)s_related')
    picture = models.FileField(upload_to='b/%Y/%m/%d', null=True, blank=True, verbose_name=_('Picture'))
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
    date_created = models.DateTimeField(auto_now_add=True)
    date_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
