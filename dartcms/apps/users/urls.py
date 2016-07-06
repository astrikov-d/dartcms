# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.config import DartCMSConfig
from dartcms.views import DeleteObjectView, GridView
from forms import UserForm
from views import ChangePasswordView, CMSUserInsertView, CMSUserUpdateView

config = DartCMSConfig({
    'model': User,
    'grid': {
        'grid_columns': (
            ('username', _('Username'), 'string', '60%'),
            ('last_login', _('Last Login'), 'datetime', '20%'),
            ('is_staff', _('Staff'), 'boolean', '10%'),
            ('is_active', _('Active'), 'boolean', '10%'),
        ),
        'grid_actions': (
            ('change-password', _('Change Password'), 'edit'),
        ),
        'template_name': 'dartcms/apps/users/grid.html'
    },
    'form': {
        'form_class': UserForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^insert/$', CMSUserInsertView.as_view(**config.form), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', CMSUserUpdateView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
]
