# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from app.models import CMSModuleGroup, CMSModule


class CMSModuleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModuleGroup, CMSModuleGroupAdmin)


class CMSModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(CMSModule, CMSModuleAdmin)
