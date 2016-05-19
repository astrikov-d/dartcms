# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from models import CMSModuleGroup, CMSModule, SiteSettings


class CMSModuleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModuleGroup, CMSModuleGroupAdmin)


class CMSModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModule, CMSModuleAdmin)


class SiteSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(SiteSettings, SiteSettingsAdmin)
