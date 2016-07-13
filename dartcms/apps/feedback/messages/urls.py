# -*- coding: utf-8 -*-
from django.conf.urls import url

from dartcms.utils.config import DartCMSConfig
from dartcms.views import GridView, UpdateObjectView, DeleteObjectView, InsertObjectView

from .views import InsertMessageForm


config = DartCMSConfig({
    'parent_kwarg_name': 'form_type',
    'parent_model_fk': 'type_id',
    'grid': {
        'grid_columns': [
            {'field': 'author', 'width': '80%'},
            {'field': 'date_created', 'width': '20%'},
        ]
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertMessageForm.as_view(**config.base), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
