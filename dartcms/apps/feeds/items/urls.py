# -*- coding: utf-8 -*-
from django.conf.urls import url

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

from .forms import FeedItemForm

FeedItem = get_model('feeds', 'FeedItem')

config = DartCMSConfig({
    'model': FeedItem,
    'parent_kwarg_name': 'feed',
    'parent_model_fk': 'feed_id',
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '60%'},
            {'field': 'is_visible', 'width': '20%'},
            {'field': 'date_published', 'width': '20%'},
        ],
        'search': [
            'name', 'date_published', 'is_visible'
        ]
    },
    'form': {
        'form_class': FeedItemForm,
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
