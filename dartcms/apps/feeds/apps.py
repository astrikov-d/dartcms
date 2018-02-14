# coding: utf-8
from dartcms.utils.fields import monkeypatch_versatile_image_field
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FeedsConfig(AppConfig):
    name = 'dartcms.apps.feeds'
    verbose_name = _('Feeds')

    def ready(self):
        monkeypatch_versatile_image_field()
