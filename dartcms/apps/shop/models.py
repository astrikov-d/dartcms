# coding: utf-8
from django.db.models import F, Max
from django.db.models.signals import post_save, pre_delete, pre_save

from dartcms.utils.loading import get_model, is_model_registered

from .abstract_models import *

__all__ = []

if not is_model_registered('shop', 'Order'):
    class Order(AbstractOrder):
        pass

    __all__.append('Order')

if not is_model_registered('shop', 'OrderDetail'):
    class OrderDetail(AbstractOrderDetail):
        pass

    __all__.append('OrderDetail')

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

if not is_model_registered('shop', 'ProductImage'):
    class ProductImage(AbstractProductImage):
        pass

    __all__.append('ProductImage')

if not is_model_registered('shop', 'ProductLabel'):
    class ProductLabel(AbstractProductLabel):
        pass

    __all__.append('ProductLabel')

if not is_model_registered('shop', 'Product'):
    class Product(AbstractProduct):
        pass

    __all__.append('Product')

if not is_model_registered('shop', 'ProductManufacturer'):
    class ProductManufacturer(AbstractProductManufacturer):
        pass

    __all__.append('ProductManufacturer')


def pre_save_handler_section(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance:
        current_level = sender.objects.filter(parent=instance.parent)

        if not current_level.exists():
            instance.sort = 1

        if not instance.id or instance.sort == 0:
            max_sort = current_level.aggregate(Max('sort'))
            s = max_sort.get('sort_max')
            instance.sort = s + 1 if s else 1
        else:
            page_cache = sender.objects.get(pk=instance.id)

            if page_cache.parent == instance.parent:
                if int(page_cache.sort) < int(instance.sort):
                    instance.sort -= 1
                    current_level.filter(sort__gt=page_cache.sort, sort__lte=instance.sort).update(
                        sort=F('sort') - 1)
                else:
                    current_level.filter(sort__gte=instance.sort, sort__lt=page_cache.sort).update(
                        sort=F('sort') + 1)
            else:
                current_level.filter(sort__gte=instance.sort).update(sort=F('sort') + 1)
                sender.objects.filter(parent=page_cache.parent, sort__gt=page_cache.sort).update(sort=F('sort') - 1)


def post_save_handler_section(**kwargs):
    instance = kwargs.get('instance')
    if instance:
        children = instance.children.all()
        if children:
            for child in instance.children.all():
                child.save()


def pre_delete_handler_section(sender, **kwargs):
    instance = kwargs.get('instance')
    if instance:
        sender.objects.filter(parent=instance.parent, sort__gt=instance.sort).update(sort=F('sort') - 1)


pre_save.connect(pre_save_handler_section, sender=section_model)
post_save.connect(post_save_handler_section, sender=section_model)
pre_delete.connect(pre_delete_handler_section, sender=section_model)
