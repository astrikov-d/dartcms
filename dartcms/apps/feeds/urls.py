# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.forms import modelform_factory

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

Feed = get_model('feeds', 'Feed')

config = DartCMSConfig({
    'model': Feed,
    'grid': {
        'grid_columns': [
            {'field': 'type', 'width': '10%'},
            {'field': 'name', 'width': '90%'},
        ],
        'additional_grid_actions': [
            {'url': 'items'}
        ]
    },
    'form': {
        'form_class': modelform_factory(Feed, exclude=[]),
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^(?P<children_url>items)/(?P<feed>\d+)/', include('dartcms.apps.feeds.items.urls', namespace='feed_items')),
]
