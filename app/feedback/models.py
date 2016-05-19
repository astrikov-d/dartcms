__author__ = 'astrikovd'

import datetime

from django.utils.translation import ugettext_lazy as _
from django.db import models


class FeedbackType(models.Model):
    """
    Feedback type. I.e. `faq` or `feedback` or `contact`
    """

    class Meta:
        verbose_name = _(u"feedback type")
        verbose_name_plural = _(u"feedback types")
        ordering = ['name']

    @property
    def messages_count(self):
        return self.messages.all().count()

    @property
    def last_message_date(self):
        return self.messages.last().date_created

    name = models.CharField(max_length=255, verbose_name=_(u"Name"))
    slug = models.SlugField(verbose_name=_(u"Slug"))


class FeedbackMessage(models.Model):
    class Meta:
        verbose_name = _(u"feedback message")
        verbose_name_plural = _(u"feedback messages")
        ordering = ['-date_created']

    def __unicode__(self):
        return "%s / %s" % (self.feedback_type.name, self.author)

    feedback_type = models.ForeignKey(FeedbackType, verbose_name=_(u"Type"), related_name='messages')
    author = models.CharField(max_length=255, verbose_name=_(u"Author"))
    email = models.EmailField(verbose_name=_(u"Contact Email"), null=True, blank=True)
    message = models.TextField(verbose_name=_(u"Message"))
    answer = models.TextField(verbose_name=_(u"Answer"))
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_published = models.DateTimeField(default=datetime.datetime.now, verbose_name=_(u"Date of Publication"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))