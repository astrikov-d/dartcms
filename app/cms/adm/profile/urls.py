# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.contrib.auth.decorators import login_required, permission_required
from django.conf.urls import patterns, url, include

from views import ProfileSettingsView

urlpatterns = patterns('',
    url(r'^$', login_required(ProfileSettingsView.as_view()), name='index'),
    url(r'^(?P<result>(success|error))/$', login_required(ProfileSettingsView.as_view()), name='index'),
)