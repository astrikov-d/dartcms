# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .views import (DeleteMessageFormView, InsertMessageFormView,
                    MessagesGridView, UpdateMessageFormView)

app_name = 'feedback_messages'

config = DartCMSConfig({
    'parent_kwarg_name': 'form_type',
    'parent_model_fk': 'type_id',
    'grid': {
        'base_grid_actions': ['update', 'delete', 'insert'],
        'grid_columns': [
            {'field': 'author', 'width': '80%', 'label': _('Author')},
            {'field': 'date_created', 'width': '20%', 'label': _('Date_created')},
        ]
    }
})

urlpatterns = [
    url(r'^$', MessagesGridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertMessageFormView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateMessageFormView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteMessageFormView.as_view(**config.base), name='delete'),
]
