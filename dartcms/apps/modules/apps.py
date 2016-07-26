# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ModulesConfig(AppConfig):
    name = 'dartcms.apps.modules'
    verbose_name = _('DartCMS Modules')
