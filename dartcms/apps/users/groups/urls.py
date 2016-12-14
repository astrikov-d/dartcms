# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.forms.models import modelform_factory

from dartcms.apps.users.models import UserGroup
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

config = DartCMSConfig({
    'model': UserGroup,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '100%'},
        ]
    },
    'form': {
        'form_class': modelform_factory(model=UserGroup, exclude=['users'])
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
