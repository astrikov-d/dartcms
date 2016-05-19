# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _
from django.forms.models import modelform_factory

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from app.adv.models import AdvSection

Form = modelform_factory(
    model=AdvSection,
    exclude=[]
)

grid_columns = (
    ('name', _(u"Name"), 'string', '80%'),
)

kwargs = {
    'model': AdvSection,
    'form_class': Form,
    'grid_columns': (
        ('name', _(u"Name"), 'string', '80%'),
    )
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
)