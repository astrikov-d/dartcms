# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class SitesettingsConfig(AppConfig):
    name = 'dartcms.apps.sitesettings'
    verbose_name = _('Site settings')
