# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from dartcms.utils.config import DartCMSConfig
from dartcms.views import GridView
from .models import FormType

config = DartCMSConfig({
    'model': FormType,
    'grid': {
        'grid_columns': [
            {'field': 'slug', 'width': '30%'},
            {'field': 'name', 'width': '70%'},
        ],
        'base_grid_actions': [],
        'additional_grid_actions': [
            {'url': 'messages'}
        ]
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^(?P<children_url>messages)/(?P<form_type>\d+)/',
        include('dartcms.apps.feedback.messages.urls', namespace='feedback_messages')),
]
