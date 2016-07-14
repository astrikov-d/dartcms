# coding: utf-8
from django.conf.urls import url
from django.forms import modelform_factory

from dartcms.apps.ads.models import AdSection
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

config = DartCMSConfig({
    'model': AdSection,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '80%'},
            {'field': 'is_enabled', 'width': '20%'},
        ]
    },
    'form': {
        'form_class': modelform_factory(AdSection, exclude=[]),
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
