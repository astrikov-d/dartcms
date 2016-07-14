# coding: utf-8
from django.conf.urls import url
from django.forms import modelform_factory

from dartcms.apps.ads.models import AdPlace
from dartcms.utils.config import DartCMSConfig
from dartcms.views import GridView, UpdateObjectView

config = DartCMSConfig({
    'model': AdPlace,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '80%'},
            {'field': 'is_enabled', 'width': '20%'},
        ],
        'base_grid_actions': ['update']
    },
    'form': {
        'form_class': modelform_factory(AdPlace, exclude=['slug']),
    },
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update')
]
