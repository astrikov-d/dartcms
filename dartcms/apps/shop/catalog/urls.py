# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from django.utils.translation import ugettext_lazy as _

from .forms import ProductCatalogForm

app_name = 'catalog'

ProductCatalog = get_model('shop', 'ProductCatalog')

config = DartCMSConfig({
    'model': ProductCatalog,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '50%'},
            {'field': 'slug', 'width': '40%'},
            {'field': 'is_visible', 'width': '10%'},
        ],
        'additional_grid_actions': [
            {'url': 'sections', 'label': _('Sections'),
             'kwarg_name': 'catalog', 'include_urls': 'dartcms.apps.shop.section.urls'}
        ]
    },
    'form': {
        'form_class': ProductCatalogForm
    }
})

urlpatterns = config.get_urls()
