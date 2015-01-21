# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from app.cms.models import CMSModuleGroup, CMSModule, SiteSettings
from models import PageModule


class PageModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(PageModule, PageModuleAdmin)
