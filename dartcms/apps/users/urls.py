# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from dartcms.views import GridView, DeleteObjectView
from views import ChangePasswordView, CMSUserUpdateView, CMSUserInsertView
from forms import UserForm

kwargs = {
    'model': User,
    'form_class': UserForm,
    'grid_columns': (
        ('username', _(u'Username'), 'string', '40%'),
        ('last_login', _(u'Last Login'), 'datetime', '20%'),
        ('is_staff', _(u'Staff'), 'boolean', '10%'),
        ('is_active', _(u'Active'), 'boolean', '10%'),
    ),
}

grid_kwargs = kwargs.copy()
grid_kwargs.update({
    'template_name': 'dartcms/apps/users/grid.html'
})

urlpatterns = [
    url(r'^$', GridView.as_view(**grid_kwargs), name='index'),
    url(r'^insert/$', CMSUserInsertView.as_view(**kwargs), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', CMSUserUpdateView.as_view(**kwargs), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**kwargs), name='delete'),
    url(r'^change-password/(?P<pk>\d+)/$', ChangePasswordView.as_view(), name='change_password'),
]
