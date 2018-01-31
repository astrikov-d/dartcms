# coding: utf-8
from dartcms.utils.config import DartCMSConfig
from django.utils.translation import ugettext_lazy as _

from .forms import SiteSettingsForm
from .models import SiteSettings

app_name = 'sitesettings'

config = DartCMSConfig({
    'model': SiteSettings,
    'grid': {
        'grid_columns': [
            {'field': 'description', 'width': '20%'},
            {'field': 'type_display', 'width': '20%', 'label': _('Type')},
            {'field': 'value_for_grid', 'width': '60%', 'label': _('Value')},
        ],
        'base_grid_actions': ['update'],
        'model_properties': ['type_display', 'value_for_grid']
    },
    'form': {
        'form_class': SiteSettingsForm,
    }
})

urlpatterns = config.get_urls(exclude=['insert', 'delete'])
