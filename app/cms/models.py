__author__ = 'astrikovd'

import datetime

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.utils.translation import get_language
from django.conf import settings


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
    user = models.ManyToManyField(User, verbose_name=_(u"User"), null=True, blank=True)
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