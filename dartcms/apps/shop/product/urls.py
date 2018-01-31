# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig

from .forms import ProductForm

app_name = 'products'

Product = get_model('shop', 'Product')

config = DartCMSConfig({
    'model': Product,
    'parent_kwarg_name': 'section',
    'parent_model_fk': 'section_id',
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '40%'},
            {'field': 'code', 'width': '20%'},
            {'field': 'manufacturer', 'width': '20%'},
            {'field': 'residue', 'width': '10%'},
            {'field': 'price', 'width': '10%'},
        ]
    },
    'form': {
        'form_class': ProductForm,
    }
})

urlpatterns = config.get_urls()
