# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig

app_name = 'ad'

Ad = get_model('ads', 'Ad')

config = DartCMSConfig({
    'model': Ad,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '30%'},
            {'field': 'place', 'width': '20%'},
            {'field': 'date_from', 'width': '20%'},
            {'field': 'date_to', 'width': '20%'},
            {'field': 'is_enabled', 'width': '10%'},
        ]
    }
})

urlpatterns = config.get_urls()
