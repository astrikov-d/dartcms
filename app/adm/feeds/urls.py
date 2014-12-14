# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from django.forms.models import modelform_factory
from app.models import Feed as Model

Form = modelform_factory(Model)

grid_columns = (
    ('name', u"Название", 'string', '100%'),
)

object_actions = (
    (u'Записи', u'items', u'fa-list-alt'),
)

kwargs = {
    'grid_columns': grid_columns,
    'object_actions': object_actions,
    'model': Model,
    'form_class': Form,
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
    url(r'^(?P<children_url>items)/(?P<feed>\d+)/', include('app.adm.feeds.items.urls', namespace='feed_items')),
)