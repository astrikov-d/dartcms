# coding: utf-8
from django.contrib import admin

from dartcms import get_model

OrderShippingType = get_model('shop', 'OrderShippingType')
OrderPaymentType = get_model('shop', 'OrderPaymentType')
OrderStatus = get_model('shop', 'OrderStatus')


class ModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderShippingType, ModelAdmin)
admin.site.register(OrderPaymentType, ModelAdmin)
admin.site.register(OrderStatus, ModelAdmin)
