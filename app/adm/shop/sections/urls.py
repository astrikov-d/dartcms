# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView
from django.forms.models import modelform_factory
from app.models import ProductSection as Model

Form = modelform_factory(Model, exclude=['slug', 'category'])

grid_columns = (
    ('name', _(u"Name"), 'string', '30%'),
    ('slug', _(u"Slug"), 'string', '30%'),
    ('products_count', _(u"Products Count"), 'string', '20%'),
    ('is_visible', _(u"Show on Site"), 'boolean', '20%'),
)

object_actions = (
    (_(u'Products'), u'products', u'fa-list-alt'),
)

kwargs = {
    'grid_columns': grid_columns,
    'object_actions': object_actions,
    'model': Model,
    'form_class': Form,
    'parent_kwarg_name': 'category',
    'parent_model_fk': 'category_id'
}

urlpatterns = patterns('',
    url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(**kwargs)), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(**kwargs)), name='delete'),
    url(r'^(?P<children_url>products)/(?P<section>\d+)/', include('app.adm.shop.products.urls', namespace='products')),
)