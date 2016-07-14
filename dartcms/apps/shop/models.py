# coding: utf-8
from django.db import models
from django.db.models import F, Max
from django.db.models.signals import post_save, pre_delete, pre_save
from django.utils.translation import ugettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey
from autoslug import AutoSlugField

from dartcms.utils.fields import RteField
from dartcms.utils.loading import get_model, is_model_registered

__all__ = [
    'pre_save_handler_section',
    'post_save_handler_section',
    'pre_delete_handler_section'
]


class AbstractProductCatalog(models.Model):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('product catalogs')
        verbose_name = _('product catalog')

    def __unicode__(self):
        return self.name

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    name = models.CharField(_('Name'), max_length=64)
    description = RteField(_('Description'), blank=True, default='')
    image = models.ImageField(_('Image'), upload_to='shop/catalog', null=True, blank=True)
    seo_keywords = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    seo_description = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    is_visible = models.BooleanField(_('Is Visible'), default=True)
    date_created = models.DateTimeField(auto_now_add=True)


if is_model_registered('shop', 'ProductCatalog'):
    catalog_model = get_model('shop', 'ProductCatalog')
else:
    class ProductCatalog(AbstractProductCatalog):
        pass

    __all__.append('ProductCatalog')

    catalog_model = ProductCatalog


class AbstractProductSection(MPTTModel):
    class Meta:
        abstract = True
        ordering = ['sort']
        verbose_name = _('product section')
        verbose_name_plural = _('product sections')
        unique_together = ['cat', 'slug']

    def __unicode__(self):
        parent = self.parent
        page_names = [self.name]
        while parent:
            page_names.append(parent.name)
            parent = parent.parent
        return ' / '.join(reversed(page_names))

    parent = TreeForeignKey('self', null=True, related_name='children', verbose_name=_('Parent Section'), blank=True)

    catalog = models.ForeignKey(ProductCatalog, verbose_name=_('Product catalog'), related_name='sections')
    slug = AutoSlugField(_('URL'), populate_from='name')
    name = models.CharField(_('Name'), max_length=255)
    description = RteField(_('Before Content'), default='', blank=True)
    image = models.ImageField(_('Image'), upload_to='cat', null=True, blank=True)
    seo_keywords = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    seo_description = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    is_enabled = models.BooleanField(_('Is Enabled'), default=True)
    sort = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def delete(self):
        if not self.parent:
            pass
        else:
            return super(AbstractProductSection, self).delete()

    def serializable_object(self):
        obj = {
            'pk': self.pk,
            'parent_id': self.parent_id,
            'name': self.name,
            'is_enabled': self.is_enabled,
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
    section_model = get_model('shop', 'ShopSection')
else:
    class ProductSection(AbstractProductSection):
        pass


    __all__.append('ShopSection')

    section_model = ProductSection

pre_save.connect(pre_save_handler_section, sender=section_model)
post_save.connect(post_save_handler_section, sender=section_model)
pre_delete.connect(pre_delete_handler_section, sender=section_model)


class AbstractProductLabel(models.Model):
     name = models.CharField(max_length=1024, verbose_name=_(u"Name"))
     slug = models.SlugField(max_length=1024, verbose_name=_(u"Slug"))
     date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


class AbstractShopProduct(models.Model):
    class Meta:
        abstract = True
        ordering = ['name']
        verbose_name_plural = _('products')
        verbose_name = _('product')

    section = models.ForeignKey(ShopSection, verbose_name=_('Section'), related_name='products')
    slug
    code
    short_description
    description
    is_available
    is_visible