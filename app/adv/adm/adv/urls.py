# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from forms import Form
from app.adv.models import Adv

grid_columns = (
    ('name', _(u"Name"), 'string', '20%'),
    ('date_from', _(u"Date of start"), 'datetime', '20%'),
    ('date_to', _(u"Date of end"), 'datetime', '20%'),
    ('is_enabled', _(u"Show on site"), 'boolean', '20%'),
)

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(
        model=Adv,
        grid_columns = grid_columns,
    )), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(
        model=Adv,
        grid_columns = grid_columns,
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