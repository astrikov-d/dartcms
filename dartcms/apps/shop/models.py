# coding: utf-8
from django.db import models
from django.db.models import F, Max
from django.db.models.signals import post_save, pre_delete, pre_save
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __

from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField

from dartcms.utils.fields import RteField
from dartcms.utils.loading import get_model, is_model_registered

__all__ = [
    'pre_save_handler_section',
    'post_save_handler_section',
    'pre_delete_handler_section'
]


class AbstractProductBase(models.Model):
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    name = models.CharField(_('Name'), max_length=255)
    description = RteField(_('Description'), blank=True, default='')
    seo_keywords = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    seo_description = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    is_visible = models.BooleanField(_('Is Visible'), default=True)
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractProductCatalog(AbstractProductBase):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('product catalogs')
        verbose_name = _('product catalog')

    slug = models.SlugField(_('URL'), unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/catalog', null=True, blank=True)

if not is_model_registered('shop', 'ProductCatalog'):
    class ProductCatalog(AbstractProductCatalog):
        pass

    __all__.append('ProductCatalog')


class AbstractProductManufacturer(AbstractProductBase):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('product manufacturers')
        verbose_name = _('product manufacturer')

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/producer', null=True, blank=True)

if not is_model_registered('shop', 'ProductManufacturer'):
    class ProductManufacturer(AbstractProductManufacturer):
        pass

    __all__.append('ProductManufacturer')


class AbstractProductSection(MPTTModel, AbstractProductBase):
    class Meta:
        abstract = True
        ordering = ['sort']
        verbose_name = _('product section')
        verbose_name_plural = _('product sections')
        unique_together = ['catalog', 'slug']

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/section', null=True, blank=True)
    parent = TreeForeignKey('self', null=True, related_name='children', verbose_name=_('Parent Section'), blank=True)
    catalog = models.ForeignKey(ProductCatalog, verbose_name=_('Product catalog'), related_name='sections')
    sort = models.IntegerField(default=1)

    def __unicode__(self):
        parent = self.parent
        section_names = [self.name]
        while parent:
            section_names.append(parent.name)
            parent = parent.parent
        return ' / '.join(reversed(section_names))

    #def delete(self, **kwargs):
    #    if not self.parent:
    #        pass
    #    else:
    #       return super(AbstractProductSection, self).delete(**kwargs)

    def serializable_object(self):
        obj = {
            'pk': self.pk,
            'parent_id': self.parent_id,
            'name': self.name,
            'is_visible': __('yes') if self.is_visible else __('no'),
            'children': []
        }
        for child in self.get_children():
            obj['children'].append(child.serializable_object())
        return obj


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


if is_model_registered('shop', 'ProductSection'):
    section_model = get_model('shop', 'ProductSection')
else:
    class ProductSection(AbstractProductSection):
        pass

    __all__.append('ProductSection')

    section_model = ProductSection

pre_save.connect(pre_save_handler_section, sender=section_model)
post_save.connect(post_save_handler_section, sender=section_model)
pre_delete.connect(pre_delete_handler_section, sender=section_model)


class AbstractProductLabel(AbstractProductBase):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('product labels')
        verbose_name = _('product label')

    slug = models.SlugField(_('URL'), unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/label', null=True, blank=True)

if not is_model_registered('shop', 'ProductLabel'):
    class ProductLabel(AbstractProductLabel):
        pass

    __all__.append('ProductLabel')


class AbstractProduct(AbstractProductBase):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('products')
        verbose_name = _('product')

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    section = models.ForeignKey(ProductSection, verbose_name=_('Section'), related_name='products')
    manufacturer = models.ForeignKey(ProductManufacturer, verbose_name=_('Manufacturer'),
                                     related_name='manufacturer_products', null=True, blank=True)
    labels = models.ManyToManyField(ProductLabel, verbose_name=_('Labels'), related_name='label_products', blank=True)
    code = models.CharField(_('Code'), max_length=100, blank=True, default='')
    short_description = RteField(_('Short description'), blank=True, default='')
    residue = models.IntegerField(_('Residue'), default=1)
    price = models.DecimalField(verbose_name=_(u"Price"), decimal_places=2, max_digits=10, default=0)
    image = models.ImageField(_('Image'), upload_to='shop/product/%Y/%m/%d', null=True, blank=True)

if not is_model_registered('shop', 'Product'):
    class Product(AbstractProduct):
        pass

    __all__.append('Product')


class AbstractProductImage(models.Model):
    class Meta:
        abstract = True
        verbose_name = _(u"product picture")
        verbose_name_plural = _(u"product pictures")
        ordering = ['-date_created']

    product = models.ForeignKey(Product, verbose_name=_(u"Product"), related_name='pictures')
    image = models.ImageField(_('Image'), upload_to="shop/product_images/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True)

if not is_model_registered('shop', 'ProductImage'):
    class ProductImage(AbstractProductImage):
        pass

    __all__.append('ProductImage')
