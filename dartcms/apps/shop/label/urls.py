# coding: utf-8
from django.conf.urls import include, url

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

from .forms import ProductLabelForm

ProductLabel = get_model('shop', 'ProductLabel')

config = DartCMSConfig({
    'model': ProductLabel,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '90%'},
            {'field': 'is_visible', 'width': '10%'},
        ],
    },
    'form': {
        'form_class': ProductLabelForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
