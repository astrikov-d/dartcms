# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from app.models import FeedbackMessage as Model
from forms import Form

grid_columns = (
    ('author', _(u"Author"), 'string', '40%'),
    ('email', _(u"Email"), 'string', '40%'),
    ('date_created', _(u"Date of Creation"), 'datetime', '20%'),
)

kwargs = {
    'grid_columns': grid_columns,
    'model': Model,
    'form_class': Form,
    'parent_kwarg_name': 'feedback_type',
    'parent_model_fk': 'feedback_type_id'
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
)