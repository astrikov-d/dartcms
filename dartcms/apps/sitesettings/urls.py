# coding: utf-8
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.config import DartCMSConfig
from dartcms.views import GridView, UpdateObjectView

from .forms import SiteSettingsForm as Form
from .models import SiteSettings

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
        'form_class': Form,
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update')
]
