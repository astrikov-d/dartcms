# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from forms import Form
from app.models import Adv

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(
        model=Adv,
        grid_columns = (
            ('name', u"Название", 'string', '20%'),
            ('date_from', u"Дата начала показов", 'datetime', '20%'),
            ('date_to', u"Дата начала показов", 'datetime', '20%'),
            ('is_enabled', u"Показывать на сайте", 'boolean', '20%'),
        ),
    )), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(
        model=Adv,
        grid_columns = (
            ('name', u"Название", 'string', '20%'),
            ('date_from', u"Дата начала показов", 'datetime', '20%'),
            ('date_to', u"Дата начала показов", 'datetime', '20%'),
            ('is_enabled', u"Показывать на сайте", 'boolean', '20%'),
        ),
    )), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(
        model=Adv,
        form_class=Form
    )), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(
        model=Adv,
        form_class=Form
    )), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(
        model=Adv
    )), name='delete'),
)