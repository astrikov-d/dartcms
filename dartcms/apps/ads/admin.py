# -*- coding: utf-8 -*-
from django.contrib import admin

from models import AdPlace


class AdPlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdPlace, AdPlaceAdmin)
