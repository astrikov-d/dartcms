from django.db import models


class CMSUserManager(models.Manager):
    def get_queryset(self):
        return super(CMSUserManager, self).get_queryset().filter(is_staff=True)

    def create(self, **kwargs):
        kwargs.update({'is_staff': True})
        return super(CMSUserManager, self).create(**kwargs)

