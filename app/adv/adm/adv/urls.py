# -*- coding: utf-8 -*-
from django.forms import DateTimeInput

__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.forms.models import modelform_factory

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from app.adv.models import Adv

Form = modelform_factory(
    model=Adv,
    exclude=[],
    widgets={
        'date_from': DateTimeInput(attrs={'class': 'datetime'}),
        'date_to': DateTimeInput(attrs={'class': 'datetime'}),
    })

grid_columns = (
    ('name', _(u"Name"), 'string', '20%'),
    ('views', _(u"Views"), 'string', '10%'),
    ('clicks_count', _(u"Clicks"), 'string', '10%'),
    ('clicks_count_uniq', _(u"Clicks (unique)"), 'string', '10%'),
    ('ctr', u"CTR, %", 'string', '10%'),
    ('date_from', _(u"Date of start"), 'datetime', '10%'),
    ('date_to', _(u"Date of end"), 'datetime', '10%'),
    ('is_enabled', _(u"Show on site"), 'boolean', '10%'),
)

kwargs = {
    'model': Adv,
    'grid_columns': grid_columns,
    'form_class': Form
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
)