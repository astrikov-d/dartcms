# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


FORM_TYPES = (
    ('contact', _('Contact form')),
    ('question', _('Questions form'))
)


@python_2_unicode_compatible
class FormType(models.Model):
    class Meta:
        app_label = 'feedback'
        verbose_name = _('Form type')
        verbose_name_plural = _('Form types')

    slug = models.SlugField(verbose_name=_('Type ID'), choices=FORM_TYPES)
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class AbstractBaseMessage(models.Model):
    class Meta:
        app_label = 'feedback'
        abstract = True

    def __str__(self):
        return self.author

    type = models.ForeignKey(FormType, verbose_name=_('Type'))
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    message = models.TextField(verbose_name=_('Message'))
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractQuestionMessage(AbstractBaseMessage):
    class Meta:
        app_label = 'feedback'
        abstract = True

    answer = models.TextField(verbose_name=_('Answer'), blank=True, null=True)
    is_visible = models.BooleanField(verbose_name=_('Is Visible'), default=False)


class AbstractContactMessage(AbstractBaseMessage):
    class Meta:
        app_label = 'feedback'
        abstract = True

    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    phone = models.CharField(max_length=64, verbose_name=_('Phone'), blank=True, null=True)
