# coding: utf-8
from dartcms.apps.auth.utils import get_user_model
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .managers import SiteUserManager

User = get_user_model()


@python_2_unicode_compatible
class SiteUser(User):
    class Meta:
        verbose_name = _('Site User')
        verbose_name_plural = _('Site Users')
        proxy = True

    def save(self, *args, **kwargs):
        self.is_staff = False
        super(SiteUser, self).save(*args, **kwargs)

    objects = SiteUserManager()
