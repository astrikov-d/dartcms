# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from views import FeedItemsListView, FeedItemDetailView

urlpatterns = patterns('',
    url(r'^(?P<page_slug>[a-zA-Z0-9_-]+)/$', FeedItemsListView.as_view(), name='list'),
    url(r'^(?P<page_slug>[a-zA-Z0-9_-]+)/page/(?P<page>(\d+))/$', FeedItemsListView.as_view(), name='list'),
    url(r'^(?P<page_slug>[a-zA-Z0-9_-]+)/(?P<pk>(\d+))/$', FeedItemDetailView.as_view(), name='detail'),
)
