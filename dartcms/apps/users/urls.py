# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from dartcms.views import DeleteObjectView, GridView
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from .forms import UserForm
from .models import CMSUser
from .views import ChangePasswordView, CMSUserInsertView, CMSUserUpdateView

app_name = "users"

config = DartCMSConfig({
    'model': CMSUser,
    'grid': {
        'grid_columns': [
            {'field': CMSUser.USERNAME_FIELD, 'width': '60%'},
            {'field': 'last_login', 'width': '20%'},
            {'field': 'is_staff', 'width': '10%'},
            {'field': 'is_active', 'width': '10%'},
        ],
        'search': [
            CMSUser.USERNAME_FIELD, 'email'
        ],
        'additional_grid_actions': [
            {
                'url': 'change-password', 'label': _('Change Password'), 'icon': 'edit',
                'required_permissions': '__all__', 'kwarg_name': 'pk'
            }
        ],
        'model_properties': [CMSUser.USERNAME_FIELD]
    },
    'form': {
        'form_class': UserForm
    }
})

urlpatterns = config.get_urls(exclude=['addition', 'insert', 'update', 'delete']) + [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', CMSUserInsertView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', CMSUserUpdateView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
]
