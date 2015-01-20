__author__ = 'astrikovd'

import datetime
from pytils.translit import slugify

from django.utils.translation import ugettext_lazy as _
from django.db import models


class ProductCategory(models.Model):
    """
    Product categories.
    """
    class Meta:
        verbose_name = _(u"product category")
        verbose_name_plural = _(u"product categories")
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if not self.id:
            while True:
                try:
                    ProductCategory.objects.get(slug=self.slug)
                    self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
                except ProductCategory.DoesNotExist:
                    break
        super(ProductCategory, self).save()

    @property
    def sections_count(self):
        return self.sections.count()

    name = models.CharField(max_length=1024, verbose_name=_(u"Name"))
    slug = models.SlugField(max_length=1024, verbose_name=_(u"Slug"))
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


class ProductSection(models.Model):
    """
    Product sections.
    """
    class Meta:
        verbose_name = _(u"product section")
        verbose_name_plural = _(u"product sections")
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if not self.id:
            while True:
                try:
                    ProductSection.objects.get(slug=self.slug)
                    self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
                except ProductSection.DoesNotExist:
                    break
        super(ProductSection, self).save()

    @property
    def products_count(self):
        return self.products.count()

    category = models.ForeignKey(
        ProductCategory,
        related_name='sections',
        verbose_name=_(u"Category"),
        #on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=1024, verbose_name=_(u"Name"))
    slug = models.SlugField(max_length=1024, verbose_name=_(u"Slug"))
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


class ProductLabel(models.Model):
    """
    Product labels. I.e. `best choice`, `new`, `sale` etc.
    """
    name = models.CharField(max_length=1024, verbose_name=_(u"Name"))
    slug = models.SlugField(max_length=1024, verbose_name=_(u"Slug"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


class Product(models.Model):
    """
    Products.
    """
    class Meta:
        verbose_name = _(u"product")
        verbose_name_plural = _(u"products")
        ordering = ['-date_created']

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        if not self.id:
            while True:
                try:
                    Product.objects.get(slug=self.slug)
                    self.slug = u"%s-%s" % (self.slug, datetime.datetime.today().strftime("%Y%m%d%H%M%S"))
                except Product.DoesNotExist:
                    break
        super(Product, self).save()

    section = models.ForeignKey(
        ProductSection,
        related_name='products',
        verbose_name=_(u"Section"),
        #on_delete=models.DO_NOTHING
    )
    name = models.CharField(max_length=1024, verbose_name=_(u"Name"))
    slug = models.SlugField(max_length=1024, verbose_name=_(u"Slug"))
    code = models.CharField(max_length=1024, verbose_name=_(u"Code"), blank=True, null=True)
    short_description = models.TextField(verbose_name=_(u"Short description"), blank=True, null=True)
    description = models.TextField(verbose_name=_(u"Description"), blank=True, null=True)
    views_count = models.IntegerField(verbose_name=_(u"Views Count"), default=0)
    price = models.DecimalField(verbose_name=_(u"Price"), decimal_places=2, max_digits=10, default=0)
    residue = models.IntegerField(default=0, verbose_name=_(u"Residue"))
    labels = models.ManyToManyField(ProductLabel, verbose_name=_(u"Labels"), null=True, blank=True)
    is_available = models.BooleanField(default=True, verbose_name=_(u"Is Available"))
    is_visible = models.BooleanField(default=True, verbose_name=_(u"Show on Site"))
    is_special_offer = models.BooleanField(default=True, verbose_name=_(u"Is Special Offer"))
    seo_keywords = models.TextField(
        verbose_name=_(u"Keywords"),
        help_text=_(u"Don't use more than 255 symbols"),
        blank=True
    )
    seo_description = models.TextField(
        verbose_name=_(u"Description"),
        help_text=_(u"Don't use more than 1024 symbols"),
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))


class ProductPicture(models.Model):
    """
    Product pictures.
    """
    class Meta:
        verbose_name = _(u"product picture")
        verbose_name_plural = _(u"product pictures")
        ordering = ['-date_created']

    product = models.ForeignKey(Product, verbose_name=_(u"Product"), related_name='pictures')
    picture = models.ImageField(verbose_name=_(u"Picture"), upload_to="shop/%Y/%m/%d")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_(u"Date of Creation"))