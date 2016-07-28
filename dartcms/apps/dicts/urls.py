# coding: utf-8
from django.conf.urls import url

from .views import GridDictsView, InsertDictsView, UpdateDictsView, DeleteDictsView


urlpatterns = [
    url(r'^$', GridDictsView.as_view(), name='index'),
    url(r'^insert/$', InsertDictsView.as_view(), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateDictsView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteDictsView.as_view(), name='delete'),
]
