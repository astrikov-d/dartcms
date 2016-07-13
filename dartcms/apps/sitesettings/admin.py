# coding: utf-8

from django.contrib import admin

from .models import SiteSettings


class SiteSettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(SiteSettings, SiteSettingsAdmin)
