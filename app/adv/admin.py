# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from models import AdvPlace


class AdvPlaceAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdvPlace, AdvPlaceAdmin)
