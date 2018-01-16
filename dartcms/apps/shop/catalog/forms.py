# coding: utf-8
from dartcms.utils.loading import get_model
from django.utils.translation import ugettext_lazy as _
from form_utils.forms import BetterModelForm


class ProductCatalogForm(BetterModelForm):
    class Meta:
        model = get_model('shop', 'ProductCatalog')
        exclude = []

        fieldsets = (
            ('main', {'fields': (
                'slug',
                'name',
                'description',
            ), 'legend': _('Main')}),
            ('seo', {'fields': (
                'seo_keywords',
                'seo_description',
            ), 'legend': _('SEO')}),
            ('advanced', {'fields': (
                'image',
                'is_visible',
            ), 'legend': _('Advanced')}))
