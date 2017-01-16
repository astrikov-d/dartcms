# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

from dartcms.apps.auth.utils import get_user_model


class UserGroup(models.Model):
    class Meta:
        verbose_name = _('User group')
        verbose_name_plural = _('User groups')
        ordering = ['name']

    name = models.CharField(max_length=64, verbose_name=_('Group name'))
    users = models.ManyToManyField(get_user_model(), related_name='user_groups')

    def __unicode__(self):
        return self.name
