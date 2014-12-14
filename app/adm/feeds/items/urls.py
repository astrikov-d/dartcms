# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from app.models import FeedItem as Model
from forms import Form

grid_columns = (
    ('name', u"Название", 'string', '40%'),
    ('date_published', u"Дата публикации", 'datetime', '40%'),
    ('is_visible', u"Показывать на сайте", 'boolean', '20%'),
)

kwargs = {
    'grid_columns': grid_columns,
    'model': Model,
    'form_class': Form,
    'parent_kwarg_name': 'feed',
    'parent_model_fk': 'feed_id'
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
)