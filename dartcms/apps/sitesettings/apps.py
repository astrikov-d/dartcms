# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SitesettingsConfig(AppConfig):
    name = 'dartcms.apps.sitesettings'
    verbose_name = _('Site settings')
