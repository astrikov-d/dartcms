# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from forms import Form
from app.models import AdvPlace

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(
        model=AdvPlace,
        allow_insert=False,
        allow_update=False,
        allow_delete=False,
        grid_columns = (
            ('name', u"Название", 'string', '80%'),
        ),
    )), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(
        model=AdvPlace,
        allow_insert=False,
        allow_update=False,
        allow_delete=False,
        grid_columns = (
            ('name', u"Название", 'string', '80%'),
        ),
    )), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(
        model=AdvPlace,
        form_class=Form
    )), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(
        model=AdvPlace,
        form_class=Form
    )), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(
        model=AdvPlace
    )), name='delete'),
)