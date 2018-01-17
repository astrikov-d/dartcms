# coding: utf-8
from dartcms.utils.loading import is_model_registered
from django.db.models.signals import post_save, pre_delete, pre_save

from .abstract_models import *
from .signals import *

__all__ = []

if not is_model_registered('shop', 'ProductCatalog'):
    class ProductCatalog(AbstractProductCatalog):
        pass

    __all__.append('ProductCatalog')

if is_model_registered('shop', 'ProductSection'):
    section_model = get_model('shop', 'ProductSection')
else:
    class ProductSection(AbstractProductSection):
        pass

    __all__.append('ProductSection')

    section_model = ProductSection

if not is_model_registered('shop', 'ProductLabel'):
    class ProductLabel(AbstractProductLabel):
        pass

    __all__.append('ProductLabel')

if not is_model_registered('shop', 'ProductManufacturer'):
    class ProductManufacturer(AbstractProductManufacturer):
        pass

    __all__.append('ProductManufacturer')

if not is_model_registered('shop', 'Product'):
    class Product(AbstractProduct):
        pass

    __all__.append('Product')

if not is_model_registered('shop', 'ProductImage'):
    class ProductImage(AbstractProductImage):
        pass

    __all__.append('ProductImage')

if not is_model_registered('shop', 'OrderStatus'):
    class OrderStatus(AbstractOrderStatus):
        pass

    __all__.append('OrderStatus')

if not is_model_registered('shop', 'OrderPaymentType'):
    class OrderPaymentType(AbstractOrderPaymentType):
        pass

    __all__.append('OrderPaymentType')

if not is_model_registered('shop', 'OrderShippingType'):
    class OrderShippingType(AbstractOrderShippingType):
        pass

    __all__.append('OrderShippingType')

if not is_model_registered('shop', 'Order'):
    class Order(AbstractOrder):
        pass

    __all__.append('Order')

if not is_model_registered('shop', 'OrderDetail'):
    class OrderDetail(AbstractOrderDetail):
        pass

    __all__.append('OrderDetail')

pre_save.connect(pre_save_handler_section, sender=section_model)
post_save.connect(post_save_handler_section, sender=section_model)
pre_delete.connect(pre_delete_handler_section, sender=section_model)
