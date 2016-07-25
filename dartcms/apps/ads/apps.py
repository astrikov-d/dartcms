# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AdsConfig(AppConfig):
    name = 'dartcms.apps.ads'
    verbose_name = _('Ads')
