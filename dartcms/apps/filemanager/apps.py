# coding: utf-8
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FileManagerConfig(AppConfig):
    name = 'dartcms.apps.filemanager'
    verbose_name = _('FileManager')
