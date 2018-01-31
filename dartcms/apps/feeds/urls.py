# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from django.forms import modelform_factory

app_name = 'feeds'

Feed = get_model('feeds', 'Feed')

config = DartCMSConfig({
    'model': Feed,
    'grid': {
        'grid_columns': [
            {'field': 'type', 'width': '10%'},
            {'field': 'name', 'width': '90%'},
        ],
        'additional_grid_actions': [
            {'url': 'items', 'kwarg_name': 'feed', 'include_urls': 'dartcms.apps.feeds.items.urls'}
        ]
    },
    'form': {
        'form_class': modelform_factory(Feed, exclude=[]),
    }
})

urlpatterns = config.get_urls()
