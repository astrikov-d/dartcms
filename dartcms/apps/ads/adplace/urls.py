# coding: utf-8
from dartcms.apps.ads.models import AdPlace
from dartcms.utils.config import DartCMSConfig
from django.forms import modelform_factory

app_name = 'adplace'

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

urlpatterns = config.get_urls(exclude=['insert', 'delete'])
