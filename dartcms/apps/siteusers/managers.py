from django.db import models


class SiteUserManager(models.Manager):
    def get_queryset(self):
        return super(SiteUserManager, self).get_queryset().filter(is_staff=False)

    def create(self, **kwargs):
        kwargs.update({'is_staff': False})
        return super(SiteUserManager, self).create(**kwargs)
