# -*- coding: utf-8 -*-
from django.conf.urls import url

from dartcms.utils.config import DartCMSConfig

from .views import MessagesGridView, UpdateMessageFormView, DeleteMessageFormView


config = DartCMSConfig({
    'parent_kwarg_name': 'form_type',
    'parent_model_fk': 'type_id',
    'grid': {
        'base_grid_actions': ['update', 'delete'],
        'grid_columns': [
            {'field': 'author', 'width': '80%'},
            {'field': 'date_created', 'width': '20%'},
        ]
    }
})

urlpatterns = [
    url(r'^$', MessagesGridView.as_view(**config.grid), name='index'),
    url(r'^update/(?P<pk>\d+)/$', UpdateMessageFormView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteMessageFormView.as_view(**config.base), name='delete'),
]
