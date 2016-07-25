# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.loading import is_model_registered

__all__ = [
    'FormType',
    'AbstractBaseMessage',
    'AbstractQuestionMessage',
    'AbstractContactMessage'
]

FORM_TYPES = (
    ('contact', _('Contact form')),
    ('question', _('Questions form'))
)


class FormType(models.Model):
    class Meta:
        verbose_name = _('Form type')
        verbose_name_plural = _('Form types')

    slug = models.SlugField(verbose_name=_('Type ID'), choices=FORM_TYPES)
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name


class AbstractBaseMessage(models.Model):
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.author

    type = models.ForeignKey(FormType, verbose_name=_('Type'))
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    message = models.TextField(verbose_name=_('Message'))
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractQuestionMessage(AbstractBaseMessage):
    class Meta:
        abstract = True

    answer = models.TextField(verbose_name=_('Answer'), blank=True, null=True)
    is_visible = models.BooleanField(verbose_name=_('Is Visible'), default=False)


class AbstractContactMessage(AbstractBaseMessage):
    class Meta:
        abstract = True

    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    phone = models.CharField(max_length=64, verbose_name=_('Phone'), blank=True, null=True)


if not is_model_registered('feedback', 'QuestionMessage'):
    class QuestionMessage(AbstractQuestionMessage):
        pass


    __all__.append('QuestionMessage')

if not is_model_registered('feedback', 'ContactMessage'):
    class ContactMessage(AbstractContactMessage):
        pass


    __all__.append('ContactMessage')
