# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from views import FeedbackIndexView, FeedbackSuccessView

urlpatterns = patterns('',
    url(r'^(?P<page_slug>[a-zA-Z0-9_-]+)/$', FeedbackIndexView.as_view(), name='list'),
    url(r'^(?P<page_slug>[a-zA-Z0-9_-]+)/success/$', FeedbackSuccessView.as_view(), name='success'),
)
