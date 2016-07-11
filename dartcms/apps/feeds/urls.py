# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.forms import modelform_factory
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import GridView, UpdateObjectView, DeleteObjectView, InsertObjectView

Feed = get_model('feeds', 'Feed')

config = DartCMSConfig({
    'model': Feed,
    'grid': {
        'grid_columns': (
            ('type', _('Type'), 'string', '30%'),
            ('name', _('Name'), 'string', '70%'),
        ),
        'grid_actions': (
            ('items', _('View Records'), 'next'),
        ),
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
