# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from django.forms.models import modelform_factory
from app.feedback.models import FeedbackType as Model

Form = modelform_factory(Model, exclude=[])

grid_columns = (
    ('name', _(u"Name"), 'string', '40%'),
    ('messages_count', _(u"Messages Count"), 'string', '30%'),
    ('last_message_date', _(u"Last Message"), 'datetime', '30%'),
)

object_actions = (
    (_(u'Records'), u'items', u'fa-list-alt'),
)

kwargs = {
    'grid_columns': grid_columns,
    'object_actions': object_actions,
    'model': Model,
    'form_class': Form,
    'allow_insert': False,
    'allow_update': False,
    'allow_delete': False,
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
    url(r'^(?P<children_url>items)/(?P<feedback_type>\d+)/', include('app.feedback.adm.items.urls', namespace='feedback_items')),
)