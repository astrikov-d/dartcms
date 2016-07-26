# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedsConfig(AppConfig):
    name = 'dartcms.apps.feeds'
    verbose_name = _('Feeds')
