# -*- coding: utf-8 -*-
from django.contrib import admin

from dartcms.utils.loading import get_model

AdPlace = get_model('ads', 'AdPlace')
AdSection = get_model('ads', 'AdSection')


class AdPlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdPlace, AdPlaceAdmin)


class AdSectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdSection, AdSectionAdmin)
