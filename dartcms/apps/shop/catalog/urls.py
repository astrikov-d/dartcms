# coding: utf-8
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

from .forms import ProductCatalogForm

ProductCatalog = get_model('shop', 'ProductCatalog')

config = DartCMSConfig({
    'model': ProductCatalog,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '50%'},
            {'field': 'slug', 'width': '40%'},
            {'field': 'is_visible', 'width': '10%'},
        ],
        'additional_grid_actions': [
            {'url': 'sections', 'label': _('Sections')}
        ]
    },
    'form': {
        'form_class': ProductCatalogForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^(?P<children_url>sections)/(?P<catalog>\d+)/', include('dartcms.apps.shop.section.urls', namespace='sections')),
]
