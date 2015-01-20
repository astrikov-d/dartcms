# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from app.cms.models import CMSModuleGroup, CMSModule
from app.pagemap.models import PageModule


class CMSModuleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModuleGroup, CMSModuleGroupAdmin)


class CMSModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModule, CMSModuleAdmin)


class PageModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(PageModule, PageModuleAdmin)
