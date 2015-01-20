# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from views import PageDetailView

urlpatterns = patterns('',
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$', PageDetailView.as_view(), name='detail'),
)
