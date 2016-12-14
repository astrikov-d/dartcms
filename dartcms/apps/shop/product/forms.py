# coding: utf-8
from django.utils.translation import ugettext_lazy as _
from form_utils.forms import BetterModelForm

from dartcms.utils.loading import get_model


class ProductForm(BetterModelForm):
    class Meta:
        model = get_model('shop', 'Product')
        exclude = ['section']

        fieldsets = (
            ('main', {'fields': (
                'slug',
                'name',
                'code',
                'short_description',
                'description',
                'manufacturer',
                'residue',
                'price',
            ), 'legend': _('Main')}),
            ('seo', {'fields': (
                'seo_keywords',
                'seo_description',
            ), 'legend': _('SEO')}),
            ('advanced', {'fields': (
                'labels',
                'image',
                'is_visible',
            ), 'legend': _('Advanced')}))
