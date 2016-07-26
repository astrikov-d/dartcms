# coding: utf-8
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.loading import get_model
from form_utils.forms import BetterModelForm


class ProductLabelForm(BetterModelForm):
    class Meta:
        model = get_model('shop', 'ProductLabel')
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
