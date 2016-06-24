# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url

from views import ClickView

urlpatterns = patterns(
    '',
    url(r'^$', ClickView.as_view(), name='click'),
)
