# coding: utf-8
from decimal import Decimal

from autoslug import AutoSlugField
from django.db import models
from django.db.models import F, Sum
from django.utils.translation import ugettext as __
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey

from dartcms.utils.fields import RteField
from dartcms.utils.loading import get_model


class AbstractProductBase(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'

    def __unicode__(self):
        return self.name

    name = models.CharField(_('Name'), max_length=255)
    description = RteField(_('Description'), blank=True, default='')
    seo_keywords = models.TextField(_('Keywords (meta keywords)'), default='', blank=True)
    seo_description = models.TextField(_('Description (meta description)'), default='', blank=True)
    is_visible = models.BooleanField(_('Is Visible'), default=True)
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractProductCatalog(AbstractProductBase):
    class Meta:
        abstract = True
        app_label = 'shop'
        ordering = ['name']
        verbose_name_plural = _('product catalogs')
        verbose_name = _('product catalog')

    slug = models.SlugField(_('URL'), unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/catalog', null=True, blank=True)


class AbstractProductManufacturer(AbstractProductBase):
    class Meta:
        abstract = True
        app_label = 'shop'
        ordering = ['name']
        verbose_name_plural = _('product manufacturers')
        verbose_name = _('product manufacturer')

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/producer', null=True, blank=True)


class AbstractProductSection(MPTTModel, AbstractProductBase):
    class Meta:
        abstract = True
        app_label = 'shop'
        ordering = ['sort']
        verbose_name = _('product section')
        verbose_name_plural = _('product sections')
        unique_together = ['catalog', 'slug']

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/section', null=True, blank=True)
    parent = TreeForeignKey('self', null=True, related_name='children', verbose_name=_('Parent Section'), blank=True)
    catalog = models.ForeignKey('shop.ProductCatalog', verbose_name=_('Product catalog'), related_name='sections')
    sort = models.IntegerField(default=1)

    def __unicode__(self):
        parent = self.parent
        section_names = [self.name]
        while parent:
            section_names.append(parent.name)
            parent = parent.parent
        return ' / '.join(reversed(section_names))

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


class AbstractProductLabel(AbstractProductBase):
    class Meta:
        abstract = True
        app_label = 'shop'
        ordering = ['name']
        verbose_name_plural = _('product labels')
        verbose_name = _('product label')

    slug = models.SlugField(_('URL'), unique=True)
    image = models.ImageField(_('Image'), upload_to='shop/label', null=True, blank=True)


class AbstractProduct(AbstractProductBase):
    class Meta:
        abstract = True
        app_label = 'shop'
        ordering = ['name']
        verbose_name_plural = _('products')
        verbose_name = _('product')

    slug = AutoSlugField(_('URL'), populate_from='name', unique=True)
    section = models.ForeignKey('shop.ProductSection', verbose_name=_('Section'), related_name='products')
    manufacturer = models.ForeignKey('shop.ProductManufacturer', verbose_name=_('Manufacturer'),
                                     related_name='manufacturer_products', null=True, blank=True)
    labels = models.ManyToManyField('shop.ProductLabel', verbose_name=_('Labels'), related_name='label_products',
                                    blank=True)
    code = models.CharField(_('Code'), max_length=100, blank=True, default='')
    short_description = RteField(_('Short description'), blank=True, default='')
    residue = models.IntegerField(_('Residue'), default=1)
    price = models.DecimalField(verbose_name=_('Price'), decimal_places=2, max_digits=10, default=0)
    image = models.ImageField(_('Image'), upload_to='shop/product/%Y/%m/%d', null=True, blank=True)


class AbstractProductImage(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _(u'product picture')
        verbose_name_plural = _(u'product pictures')
        ordering = ['-date_created']

    product = models.ForeignKey('shop.Product', verbose_name=_('Product'), related_name='pictures')
    image = models.ImageField(_('Image'), upload_to='shop/product_images/%Y/%m/%d')
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractOrderShippingType(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _('shipping type')
        verbose_name_plural = _('shipping types')
        ordering = ['sort']

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.cost)

    slug = models.SlugField(_('URL'), unique=True)
    name = models.CharField(_('Name'), max_length=100)
    description = RteField(_('Description'), blank=True, default='')
    cost = models.DecimalField(_('Cost'), decimal_places=2, max_digits=10, default=0)
    is_enabled = models.BooleanField(_('Is enabled'), default=True)
    sort = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractOrderPaymentType(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _('payment type')
        verbose_name_plural = _('payment types')
        ordering = ['sort']

    def __unicode__(self):
        return self.name

    slug = models.SlugField(_('URL'), unique=True)
    name = models.CharField(_('Name'), max_length=100)
    description = RteField(_('Description'), blank=True, default='')
    is_enabled = models.BooleanField(_('Is enabled'), default=True)
    sort = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractOrderStatus(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _('order status')
        verbose_name_plural = _('order statuses')
        ordering = ['sort']

    def __unicode__(self):
        return self.name

    slug = models.SlugField(_('URL'), unique=True)
    name = models.CharField(_('Name'), max_length=100)
    description = RteField(_('Description'), blank=True, default='')
    is_enabled = models.BooleanField(_('Is enabled'), default=True)
    sort = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)


class AbstractOrder(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        ordering = ['-date_created']

    fullname = models.CharField(_('Fullname'), max_length=255)
    email = models.EmailField(_('E-mail'), null=True, blank=True)
    shipping_address = models.TextField(_('Shipping address'), null=True, blank=True)

    status = models.ForeignKey('shop.OrderStatus', verbose_name=_('Status'), null=True, blank=True,
                               on_delete=models.SET_NULL)
    shipping_type = models.ForeignKey('shop.OrderShippingType', verbose_name=_('Shipping type'), null=True, blank=True,
                                      on_delete=models.SET_NULL)
    shipping_cost = models.DecimalField(verbose_name=_('Cost'), decimal_places=2, max_digits=10, default=0)
    payment_type = models.ForeignKey('shop.OrderPaymentType', verbose_name=_('Payment type'), null=True, blank=True,
                                     on_delete=models.SET_NULL)

    is_paid = models.BooleanField(_('Is paid'), default=False)
    paid_sum = models.DecimalField(_('Paid sum'), decimal_places=2, max_digits=10, null=True, blank=True)
    discount_percent = models.DecimalField(_('Discount'), decimal_places=2, max_digits=5, default=0)

    date_created = models.DateTimeField(_('Date created'), auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s%s' % (_('Order #'), self.id)

    @property
    def order_number(self):
        return self.id

    @property
    def sum_value(self):
        model = get_model('shop', 'OrderDetail')
        sum_value = model.objects.filter(order=self).aggregate(
            sum_value=Sum(F('price') * F('quantity'), output_field=models.DecimalField()))['sum_value']
        if not sum_value:
            sum_value = 0
        return sum_value

    @property
    def discount_value(self):
        return self.sum_value * self.discount_percent / 100

    @property
    def quantity(self):
        model = get_model('shop', 'OrderDetail')
        quantity = model.objects.filter(order=self).aggregate(
            quantity=Sum('quantity'))['quantity']
        if not quantity:
            quantity = 0
        return quantity

    @property
    def total(self):
        return self.sum_value + self.shipping_cost - self.discount_value


class AbstractOrderDetail(models.Model):
    class Meta:
        abstract = True
        app_label = 'shop'
        verbose_name = _('order datail')
        verbose_name_plural = _('order datails')
        ordering = ['name']

    order = models.ForeignKey('shop.Order', verbose_name=_('Order'), related_name='details')
    product = models.ForeignKey('shop.Product', null=True, on_delete=models.SET_NULL, verbose_name=_('Product'))
    code = models.CharField(_('Code'), max_length=255, blank=True)
    name = models.CharField(_('Name'), max_length=1024)
    price = models.DecimalField(_('Price'), decimal_places=2, max_digits=10, default=0)
    quantity = models.IntegerField(_('Quantity'), default=0)

    def __unicode__(self):
        return self.name

    @property
    def sum_value(self):
        return self.price * self.quantity
