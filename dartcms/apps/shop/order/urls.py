# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from django.utils.translation import ugettext_lazy as _

from .forms import OrderForm

app_name = 'orders'

Order = get_model('shop', 'Order')

config = DartCMSConfig({
    'model': Order,
    'grid': {
        'grid_columns': [
            {'field': 'order_number', 'width': '10%', 'label': _('#')},
            {'field': 'date_created', 'width': '20%'},
            {'field': 'fullname', 'width': '30%'},
            {'field': 'status', 'width': '10%'},
            {'field': 'shipping_type', 'width': '10%'},
            {'field': 'payment_type', 'width': '10%'},
            {'field': 'total', 'width': '10%', 'label': _('Total')}
        ],
        'search': [
            'fullname', 'date_created'
        ],
        'base_grid_actions': ['update'],
        'additional_grid_actions': [
            {'url': 'details', 'label': _('Details'),
             'kwarg_name': 'order', 'include_urls': 'dartcms.apps.shop.order_detail.urls'}
        ],
        'model_properties': ['order_number', 'total']
    },
    'form': {
        'form_class': OrderForm
    }
})

urlpatterns = config.get_urls(exclude=['insert', 'delete'])
