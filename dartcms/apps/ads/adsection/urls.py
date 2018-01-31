# coding: utf-8
from dartcms.apps.ads.models import AdSection
from dartcms.utils.config import DartCMSConfig

app_name = 'adsection'

config = DartCMSConfig({
    'model': AdSection,
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '80%'},
            {'field': 'is_enabled', 'width': '20%'},
        ]
    }
})

urlpatterns = config.get_urls()
