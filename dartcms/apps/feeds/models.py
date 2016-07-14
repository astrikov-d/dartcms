# coding: utf-8
import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.fields import RteField
from dartcms.utils.loading import is_model_registered

__all__ = [
    'FeedType',
    'Feed'
]


class FeedType(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_('Name'))
    slug = models.SlugField(verbose_name=_('Slug'))


class Feed(models.Model):
    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

    type = models.ForeignKey(FeedType, verbose_name=_('Type'), related_name='feeds')
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def delete(self, **kwargs):
        try:
            return super(Feed, self).delete(**kwargs)
        except models.ProtectedError:
            #todo raise exeption and show it by messages framework
            pass


class AbstractFeedItem(models.Model):
    class Meta:
        ordering = ['-date_published']
        abstract = True

    @property
    def search_content_type(self):
        return self.feed.type.slug

    def __unicode__(self):
        return self.name

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
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_('Date of Publication'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Date of Creation'))

if not is_model_registered('feeds', 'FeedItem'):
    class FeedItem(AbstractFeedItem):
        pass

    __all__.append('FeedItem')
