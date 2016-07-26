# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PagesConfig(AppConfig):
    name = 'dartcms.apps.pages'
    verbose_name = _('Pages')
