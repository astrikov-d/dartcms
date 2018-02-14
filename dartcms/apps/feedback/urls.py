# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig

from .models import FormType

app_name = 'feedback'

config = DartCMSConfig({
    'model': FormType,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '70%'},
            {'field': 'slug', 'width': '30%'},
        ],
        'additional_grid_actions': [
            {'url': 'messages', 'kwarg_name': 'form_type', 'include_urls': 'dartcms.apps.feedback.messages.urls'}
        ]
    },
})

urlpatterns = config.get_urls()
