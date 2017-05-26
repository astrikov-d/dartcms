# coding: utf-8
from django.contrib import admin

from .models import Module, ModuleGroup, ModulePermission


class ModuleGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModuleGroup, ModuleGroupAdmin)


class ModuleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Module, ModuleAdmin)


class ModulePermissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(ModulePermission, ModulePermissionAdmin)
