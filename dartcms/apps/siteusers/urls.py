# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.config import DartCMSConfig
from dartcms.views import DeleteObjectView, GridView, InsertObjectView, UpdateObjectView
from .forms import UserForm
from .views import ChangePasswordView

from .models import SiteUser

config = DartCMSConfig({
    'model': SiteUser,
    'grid': {
        'grid_columns': [
            {'field': 'username', 'width': '60%'},
            {'field': 'last_login', 'width': '20%'},
            {'field': 'is_staff', 'width': '10%'},
            {'field': 'is_active', 'width': '10%'},
        ],
        'additional_grid_actions': [
            {
                'url': 'change-password', 'label': _('Change Password'), 'icon': 'edit',
                'required_permissions': '__all__'
            }
        ],
        'model_properties': ['username']
    },
    'form': {
        'form_class': UserForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
]
