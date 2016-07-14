# coding: utf-8
from datetime import datetime

from django.db import models
from django.template.defaultfilters import striptags, truncatewords
from django.utils.translation import ugettext_lazy as _


class SiteSettings(models.Model):
    TEXT = 'text'
    TEXTAREA = 'textarea'
    RICH = 'rich'
    DATE = 'date'
    FILE = 'file'
    SELECT = 'select'

    TYPE_CHOICES = (
        (TEXT, _(u'String')),
        (TEXTAREA, _(u'Text')),
        (RICH, _(u'Rich Editor')),
        (SELECT, _(u'Select')),
        (DATE, _(u'Date')),
        (FILE, _(u'File')),
    )

    class Meta:
        ordering = ['slug']
        verbose_name = _('Site setting')
        verbose_name_plural = _('Site settings')

    def __unicode__(self):
        return u'%s - %s' % (self.slug, self.description)

    @property
    def value(self):
        return {
            self.DATE: self.date_value,
            self.FILE: self.file_value
        }.get(self.type, self.text_value)

    @property
    def type_display(self):
        return self.get_type_display()

    @property
    def value_for_grid(self):
        return truncatewords(striptags(self.value), 10)

    slug = models.SlugField(_('Identifier'), max_length=30, unique=True)
    description = models.TextField(_('Description'), default='')
    type = models.CharField(_('Type'), max_length=10, choices=TYPE_CHOICES, default=TEXT, blank=True)
    text_value = models.TextField(_('Value for text type'), default='', blank=True)
    date_value = models.DateTimeField(_('Value for date type'), blank=True, null=True, default=datetime.now)
    file_value = models.FileField(_('Value for file'), upload_to='vars', blank=True, null=True)
    options = models.TextField(_('Options for select type (use ";" as separator)'), default='', blank=True)
