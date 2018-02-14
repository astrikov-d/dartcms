# coding: utf-8
from dartcms.utils.fields import monkeypatch_versatile_image_field
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShopConfig(AppConfig):
    name = 'dartcms.apps.shop'
    verbose_name = _('Shop')

    def ready(self):
        monkeypatch_versatile_image_field()
