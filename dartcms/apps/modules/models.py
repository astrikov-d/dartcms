# coding: utf-8
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language


class ModuleGroup(models.Model):
    class Meta:
        verbose_name_plural = _('Module Groups')
        verbose_name = _('Module Group')
        ordering = ['sort']

    def __unicode__(self):
        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.name
        else:
            return self.name_en

    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    name = models.CharField(max_length=64, verbose_name=_('Name (RU)'))
    name_en = models.CharField(max_length=64, verbose_name=_('Name (EN)'))
    fa = models.SlugField(verbose_name=_('FontAwesome class'))
    sort = models.IntegerField(default=1, verbose_name=_('Sort'))
    description = models.TextField(default='', verbose_name=_('Description'), blank=True)


class Module(models.Model):
    class Meta:
        verbose_name_plural = _('Modules')
        verbose_name = _('Module')
        ordering = ['group', 'sort']

    def __unicode__(self):
        lang = get_language()
        if lang == settings.LANGUAGE_CODE:
            return self.group.name + ' / ' + self.name
        else:
            return self.group.name_en + ' / ' + self.name_en

    group = models.ForeignKey(ModuleGroup, to_field='slug', verbose_name=_('Group'), related_name='modules')
    name = models.CharField(max_length=64, verbose_name=_('Name (RU)'))
    name_en = models.CharField(max_length=64, verbose_name=_('Name (EN)'))
    sort = models.IntegerField(default=1, verbose_name=_('Sort'))
    description = models.TextField(default='', verbose_name=_('Description'), blank=True)
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    user = models.ManyToManyField(User, verbose_name=_('User'))
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
