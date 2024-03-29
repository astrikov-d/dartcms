from dartcms.utils.loading import get_model
from django.forms import HiddenInput
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm


class ProductSectionForm(ModelForm):
    class Meta:
        model = get_model('shop', 'ProductSection')
        exclude = ['catalog', 'sort']

        widgets = {'parent': HiddenInput()}

        fieldsets = (
            ('main', {'fields': (
                'parent',
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
