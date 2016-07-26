# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShopConfig(AppConfig):
    name = 'dartcms.apps.shop'
    verbose_name = _('Shop')
