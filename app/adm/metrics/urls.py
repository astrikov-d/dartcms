# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from views import ChangeSettings

urlpatterns = patterns('',
    url(r'^$', login_required(ChangeSettings.as_view()), name='index'),
)
