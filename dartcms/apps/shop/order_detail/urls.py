# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig

from .forms import OrderDatailForm

app_name = 'order_details'

Order = get_model('shop', 'OrderDetail')

config = DartCMSConfig({
    'model': Order,
    'parent_kwarg_name': 'order',
    'parent_model_fk': 'order_id',
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '60%'},
            {'field': 'price', 'width': '20%'},
            {'field': 'quantity', 'width': '20%'},
        ],
        'base_grid_actions': ['update', 'delete'],
    },
    'form': {
        'form_class': OrderDatailForm
    }
})

urlpatterns = config.get_urls(exclude=['insert'])
