# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import GridView, UpdateObjectView, DeleteObjectView, InsertObjectView

from .forms import FeedItemForm

FeedItem = get_model('feeds', 'FeedItem')

config = DartCMSConfig({
    'model': FeedItem,
    'parent_kwarg_name': 'feed',
    'parent_model_fk': 'feed_id',
    'grid': {
        'grid_columns': (
            ('name', _('Name'), 'string', '60%'),
            ('is_visible', _('Is Visible'), 'boolean', '20%'),
            ('date_published', _('Date of Publication'), 'datetime', '20%'),
        )
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