# coding: utf-8
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from jsonfield import JSONField


@python_2_unicode_compatible
class ModuleGroup(models.Model):
    class Meta:
        verbose_name_plural = _('Module Groups')
        verbose_name = _('Module Group')
        ordering = ['sort']

    def __str__(self):
        return self.name

    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    fa = models.SlugField(verbose_name=_('FontAwesome class'))
    sort = models.IntegerField(default=1, verbose_name=_('Sort'))
    description = models.TextField(default='', verbose_name=_('Description'), blank=True)


@python_2_unicode_compatible
class Module(models.Model):
    class Meta:
        verbose_name_plural = _('Modules')
        verbose_name = _('Module')
        ordering = ['group', 'sort']

    def __str__(self):
        return self.group.name + ' / ' + self.name

    group = models.ForeignKey(ModuleGroup, to_field='slug', verbose_name=_('Group'), related_name='modules')
    name = models.CharField(max_length=64, verbose_name=_('Name'))
    sort = models.IntegerField(default=1, verbose_name=_('Sort'))
    description = models.TextField(default='', verbose_name=_('Description'), blank=True)
    slug = models.SlugField(unique=True, verbose_name=_('Slug'))
    config = JSONField(null=True, blank=True, verbose_name=_('Config'))
    user = models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=_('User'))
    is_enabled = models.BooleanField(default=True, verbose_name=_('Is Enabled'))
