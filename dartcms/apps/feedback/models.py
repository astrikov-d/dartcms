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
    slug = models.SlugField(verbose_name=_('Type ID'), choices=FORM_TYPES)
    name = models.CharField(max_length=255, verbose_name=_('Name'))

    def __unicode__(self):
        return self.name


class AbstractBaseMessage(models.Model):
    class Meta:
        abstract = True

    type = models.ForeignKey(FormType, verbose_name=_('Type'))
    author = models.CharField(max_length=255, verbose_name=_('Author'))
    message = models.TextField(verbose_name=_('Message'))
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractQuestionMessage(AbstractBaseMessage):
    class Meta:
        abstract = True


class AbstractContactMessage(AbstractBaseMessage):
    class Meta:
        abstract = True

    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    phone = models.CharField(verbose_name=_('Phone'), blank=True, null=True)


if not is_model_registered('feedback', 'QuestionMessage'):
    class QuestionMessage(AbstractQuestionMessage):
        pass

    __all__.append('QuestionMessage')

if not is_model_registered('feedback', 'ContactMessage'):
    class ContactMessage(AbstractContactMessage):
        pass

    __all__.append('ContactMessage')
