from django.contrib.auth.base_user import BaseUserManager


class CMSUserManager(BaseUserManager):
    def get_queryset(self):
        return super(CMSUserManager, self).get_queryset().filter(is_staff=True)

    def create(self, **kwargs):
        kwargs.update({'is_staff': True})
        return super(CMSUserManager, self).create(**kwargs)
