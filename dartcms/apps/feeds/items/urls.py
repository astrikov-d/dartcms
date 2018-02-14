# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model

from .forms import FeedItemForm

app_name = 'feeditems'

FeedItem = get_model('feeds', 'FeedItem')

config = DartCMSConfig({
    'model': FeedItem,
    'parent_kwarg_name': 'feed',
    'parent_model_fk': 'feed_id',
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '60%'},
            {'field': 'is_visible', 'width': '20%'},
            {'field': 'date_published', 'width': '20%'},
        ],
        'search': [
            'name', 'date_published', 'is_visible'
        ]
    },
    'form': {
        'form_class': FeedItemForm,
    }
})

urlpatterns = config.get_urls()
