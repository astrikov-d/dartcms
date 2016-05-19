# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, InsertObjectView, DeleteObjectView
from views import ChangePasswordView, CMSUserUpdateView, CMSUserInsertView
from forms import CMSUserForm as Form

kwargs = {
    'model': User,
    'form_class': Form,
    'grid_columns': (
        ('username', _(u'Username'), 'string', '40%'),
        ('last_login', _(u'Last Login'), 'datetime', '20%'),
        ('is_staff', _(u'Staff'), 'boolean', '10%'),
        ('is_active', _(u'Active'), 'boolean', '10%'),
    ),
}

grid_kwargs = kwargs.copy()
grid_kwargs.update({
   'template_name': 'adm/cmsusers/grid.html'
})

urlpatterns = patterns('',
   url(r'^$', login_required(GridView.as_view(**grid_kwargs)), name='index'),
   url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**grid_kwargs)), name='index'),
   url(r'^insert/$', login_required(CMSUserInsertView.as_view(**kwargs)), name='insert'),
   url(r'^update/(?P<pk>\d+)/$', login_required(CMSUserUpdateView.as_view(**kwargs)), name='update'),
   url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
   url(r'^change-password/(?P<pk>\d+)/$', login_required(ChangePasswordView.as_view()),
       name='change_password'),
)