# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ModulesAppConfig(AppConfig):
    name = 'dartcms.apps.modules'
    verbose_name = _('DartCMS Modules')
