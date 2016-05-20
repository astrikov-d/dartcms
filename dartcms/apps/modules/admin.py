# coding: utf-8
from django.contrib import admin

from models import ModuleGroup, Module


class ModuleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModuleGroup, ModuleGroupAdmin)


class ModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Module, ModuleAdmin)
