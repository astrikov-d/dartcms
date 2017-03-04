# coding: utf-8
from django.contrib import admin

from .models import FeedType


class FeedTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(FeedType, FeedTypeAdmin)
