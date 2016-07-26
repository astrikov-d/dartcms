# coding: utf-8
from django.conf.urls import url

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import DeleteObjectView, GridView, UpdateObjectView

from .forms import OrderDatailForm

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

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
