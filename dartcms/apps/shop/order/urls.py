# coding: utf-8
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import GridView, UpdateObjectView

from .forms import OrderForm

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
            {'url': 'details', 'label': _('Details')}
        ],
        'model_properties': ['order_number', 'total']
    },
    'form': {
        'form_class': OrderForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^(?P<children_url>details)/(?P<order>\d+)/', include('dartcms.apps.shop.order_detail.urls',
                                                               namespace='order_datails')),
]
