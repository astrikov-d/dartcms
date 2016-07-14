# coding: utf-8
from django.conf.urls import url
from django.forms import DateTimeInput, modelform_factory

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

Ad = get_model('ads', 'Ad')

config = DartCMSConfig({
    'model': Ad,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '30%'},
            {'field': 'place', 'width': '20%'},
            {'field': 'date_from', 'width': '20%'},
            {'field': 'date_to', 'width': '20%'},
            {'field': 'is_enabled', 'width': '10%'},
        ]
    },
    'form': {
        'form_class': modelform_factory(Ad, exclude=[]),
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
