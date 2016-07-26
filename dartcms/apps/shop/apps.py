# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig

class ShopConfig(AppConfig):
    name = 'dartcms.apps.shop'
    verbose_name = _('Shop')
