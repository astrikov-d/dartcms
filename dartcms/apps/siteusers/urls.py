# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .forms import UserForm
from .models import SiteUser
from .views import ChangePasswordView

app_name = 'siteusers'

config = DartCMSConfig({
    'model': SiteUser,
    'grid': {
        'grid_columns': [
            {'field': SiteUser.USERNAME_FIELD, 'width': '60%'},
            {'field': 'last_login', 'width': '20%'},
            {'field': 'is_staff', 'width': '10%'},
            {'field': 'is_active', 'width': '10%'},
        ],
        'search': [
            SiteUser.USERNAME_FIELD, 'email'
        ],
        'additional_grid_actions': [
            {
                'url': 'change-password', 'label': _('Change Password'), 'icon': 'edit',
                'required_permissions': '__all__', 'kwarg_name': 'pk'
            }
        ],
        'model_properties': [SiteUser.USERNAME_FIELD]
    },
    'form': {
        'form_class': UserForm
    }
})

urlpatterns = config.get_urls(exclude=['addition']) + [
    url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
]
