# coding: utf-8
from dartcms import get_model
from django.contrib import admin

OrderShippingType = get_model('shop', 'OrderShippingType')
OrderPaymentType = get_model('shop', 'OrderPaymentType')
OrderStatus = get_model('shop', 'OrderStatus')


class ModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(OrderShippingType, ModelAdmin)
admin.site.register(OrderPaymentType, ModelAdmin)
admin.site.register(OrderStatus, ModelAdmin)
