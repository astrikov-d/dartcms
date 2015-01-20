# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url, include

from views import LoginView, LogoutView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', login_required(LogoutView.as_view()), name='logout'),
)