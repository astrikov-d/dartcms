# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AdsConfig(AppConfig):
    name = 'dartcms.apps.ads'
    verbose_name = _('Ads')
