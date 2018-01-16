# coding: utf-8
from dartcms.apps.auth.utils import get_user_model
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .managers import CMSUserManager

User = get_user_model()


@python_2_unicode_compatible
class UserGroup(models.Model):
    class Meta:
        verbose_name = _('User group')
        verbose_name_plural = _('User groups')
        ordering = ['name']

    name = models.CharField(max_length=64, verbose_name=_('Group name'))
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user_groups')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class CMSUser(User):
    class Meta:
        verbose_name = _('CMS User')
        verbose_name_plural = _('CMS Users')
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = True
        super(CMSUser, self).save(*args, **kwargs)

    objects = CMSUserManager()
