# coding: utf-8
from datetime import datetime

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import striptags, truncatewords
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class SiteSettings(models.Model):
    TEXT = 'text'
    TEXTAREA = 'textarea'
    RICH = 'rich'
    DATE = 'date'
    FILE = 'file'
    SELECT = 'select'
    OBJECT = 'object'
    BOOLEAN = 'boolean'

    TYPE_CHOICES = (
        (TEXT, _('String')),
        (TEXTAREA, _('Text')),
        (RICH, _('Rich Editor')),
        (SELECT, _('Select')),
        (DATE, _('Date')),
        (FILE, _('File')),
        (OBJECT, _('Object')),
        (BOOLEAN, _('Checkbox')),
    )

    class Meta:
        ordering = ['slug']
        verbose_name = _('Site setting')
        verbose_name_plural = _('Site settings')

    def __str__(self):
        return '%s - %s' % (self.slug, self.description)

    @property
    def value(self):
        value = ''
        if self.type == self.OBJECT and self.content_type and self.object_id:
            value = self.content_type.model_class().objects.get(pk=self.object_id)

        return {
            self.DATE: self.date_value,
            self.FILE: self.file_value,
            self.BOOLEAN: 'Да' if self.boolean_value else 'Нет',
            self.OBJECT: value,
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
    boolean_value = models.BooleanField(_('Value for boolean'), default=False)
    options = models.TextField(_('Options for select type (use ";" as separator)'), default='', blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')
