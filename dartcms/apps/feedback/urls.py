# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.forms import modelform_factory

from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

from .models import FormType

config = DartCMSConfig({
    'model': FormType,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '70%'},
            {'field': 'slug', 'width': '30%'},
        ],
        'additional_grid_actions': [
            {'url': 'messages'}
        ]
    },
    'form': {
        'form_class': modelform_factory(FormType, exclude=[]),
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^(?P<children_url>messages)/(?P<form_type>\d+)/',
        include('dartcms.apps.feedback.messages.urls', namespace='feedback_messages')),
]
