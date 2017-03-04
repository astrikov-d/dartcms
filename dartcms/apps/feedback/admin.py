# coding: utf-8
from django.contrib import admin

from .models import FormType


class FormTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(FormType, FormTypeAdmin)
