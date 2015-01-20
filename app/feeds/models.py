__author__ = 'astrikovd'

import datetime
from pytils.translit import slugify
import watson

from django.utils.translation import ugettext_lazy as _
from django.db import models


class FeedType(models.Model):
    """
    Feed type. I.e. `articles` or `news`
    """

    class Meta:
        verbose_name = _(u"feed type")
        verbose_name_plural = _(u"feed types")

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"Slug"))


class Feed(models.Model):
    class Meta:
        verbose_name = _(u"feed category")
        verbose_name_plural = _(u"feed categories")
        ordering = ['name']
        unique_together = ['type', 'slug']

    def __unicode__(self):
        return self.name

    type = models.ForeignKey(FeedType, verbose_name=_(u"Type"), related_name="feeds")
    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"URL"))


class FeedItem(models.Model):
    class Meta:
        verbose_name = _(u"feed item")
        verbose_name_plural = _(u"feed items")
        ordering = ['-date_published']

    @property
    def search_content_type(self):
        return self.feed.type.slug

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if not self.id:
            while True:
                try:
                    FeedItem.objects.get(slug=self.slug)
                    self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
                except FeedItem.DoesNotExist:
                    break
        super(FeedItem, self).save()

    feed = models.ForeignKey(Feed, verbose_name=_(u"Feed"))
    name = models.CharField(max_length=1024, verbose_name=_(u"Title"))
    slug = models.SlugField(unique=True, verbose_name=_(u"Slug"))
    short_text = models.TextField(verbose_name=_(u"Short Text"))
    full_text = models.TextField(verbose_name=_(u"Full Text"))
    picture = models.ImageField(verbose_name=_(u"Picture"), upload_to="feeds/%Y/%m/%d")
    seo_keywords = models.TextField(
        verbose_name=_(u"Keywords"),
        help_text=_(u"Don't use more than 255 symbols"),
        blank=True
    )
    seo_description = models.TextField(
        verbose_name=_(u"Description"),
        help_text=_(u"Don't use more than 1024 symbols"),
        blank=True
    )
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_(u"Date of Publication"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


watson.register(FeedItem)