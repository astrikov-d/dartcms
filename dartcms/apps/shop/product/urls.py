# coding: utf-8
from django.conf.urls import url

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

from .forms import ProductForm

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

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
