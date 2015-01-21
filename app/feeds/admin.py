# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib import admin

from models import FeedType


class FeedTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeedType, FeedTypeAdmin)
