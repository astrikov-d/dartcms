# coding: utf-8
import datetime

from autoslug import AutoSlugField
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from dartcms.utils.fields import RteField


@python_2_unicode_compatible
class FeedType(models.Model):
    class Meta:
        app_label = 'feeds'
        verbose_name = _('Feed type')
        verbose_name_plural = _('Feed types')

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(verbose_name=_('Slug'))


@python_2_unicode_compatible
class Feed(models.Model):
    class Meta:
        app_label = 'feeds'
        ordering = ['name']
        verbose_name = _('Feed')
        verbose_name_plural = _('Feeds')

    def __str__(self):
        return self.name

    type = models.ForeignKey(FeedType, verbose_name=_('Type'), related_name='feeds')
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def delete(self, **kwargs):
        try:
            return super(Feed, self).delete(**kwargs)
        except models.ProtectedError:
            # todo raise exeption and show it by messages framework
            pass


@python_2_unicode_compatible
class AbstractFeedItem(models.Model):
    class Meta:
        app_label = 'feeds'
        ordering = ['-date_published']
        abstract = True
        verbose_name = _('Feed item')
        verbose_name_plural = _('Feed items')

    @property
    def search_content_type(self):
        return self.feed.type.slug

    def __str__(self):
        return self.name

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    feed = models.ForeignKey(Feed, verbose_name=_('Feed'), on_delete=models.PROTECT)
    name = models.CharField(max_length=1024, verbose_name=_('Title'))
    short_text = RteField(verbose_name=_('Short Text'))
    full_text = RteField(verbose_name=_('Full Text'))
    picture = models.ImageField(verbose_name=_('Picture'), upload_to='feeds/%Y/%m/%d', null=True, blank=True)
    seo_keywords = models.TextField(
        verbose_name=_('Keywords'),
        help_text=_('Do not use more than 255 symbols'),
        blank=True
    )
    seo_description = models.TextField(
        verbose_name=_('Description'),
        help_text=_('Do not use more than 1024 symbols'),
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name=_('Show on Site'))
    is_main = models.BooleanField(default=True, verbose_name=_('Is Main'))
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_('Date of Publication'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of Creation'))
