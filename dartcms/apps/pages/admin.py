# -*- coding: utf-8 -*-
from dartcms.utils.loading import get_model
from django.contrib import admin

PageModule = get_model('pages', 'PageModule')
Page = get_model('pages', 'Page')


class PageModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(PageModule, PageModuleAdmin)


class PageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
