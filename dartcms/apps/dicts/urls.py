# coding: utf-8
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)
from django.conf.urls import url

app_name = 'dicts'

urlpatterns = [
    url(r'^$', GridView.as_view(search=['name']), name='index'),
    url(r'^insert/$', InsertObjectView.as_view(), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(), name='delete'),
]
