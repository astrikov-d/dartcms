__author__ = 'astrikovd'

import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.translation import get_language
from django.conf import settings
from django.template.defaultfilters import striptags, truncatewords


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
    user = models.ManyToManyField(User, verbose_name=_(u"User"))
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
    date_created = models.DateTimeField(auto_now_add=True)


class File(models.Model):
    folder = models.ForeignKey(Folder)
    path = models.FileField(upload_to="uploads/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True)


@receiver(pre_delete, sender=File)
def files_delete(sender, instance, **kwargs):
    """
    On file delete, we should also delete the file.
    """
    instance.path.delete(False)


class SiteSettings(models.Model):
    TEXT = u'text'
    TEXTAREA = u'textarea'
    RICH = u'rich'
    DATE = u'date'
    FILE = u'file'
    SELECT = u'select'

    TYPE_CHOICES = (
        (TEXT, _(u'String')),
        (TEXTAREA, _(u'Text')),
        (RICH, _(u'Rich Editor')),
        (SELECT, _(u'Select')),
        (DATE, _(u'Date')),
        (FILE, _(u'File')),
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = _(u'Site settings')
        verbose_name = _(u'Site setting')

    def __unicode__(self):
        return self.name

    @property
    def value(self):
        if self.type == self.DATE:
            return self.date_value
        if self.type == self.FILE:
            return self.file_value
        return self.text_value

    @property
    def type_display(self):
        return self.get_type_display()

    @property
    def value_for_grid(self):
        return truncatewords(striptags(self.value), 10)

    name = models.CharField(max_length=30, unique=True)
    descr = models.TextField(default='')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default=TEXT, blank=True)
    text_value = models.TextField(default='', blank=True)
    date_value = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    file_value = models.FileField(upload_to='vars', blank=True, null=True)
    options = models.TextField(default='', blank=True)
