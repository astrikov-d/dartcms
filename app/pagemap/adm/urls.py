# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import SortableTreeGridMoveView, InsertObjectView, UpdateObjectView, DeleteObjectView
from forms import Form
from app.pagemap.models import Page
from views import PagemapView, PageModuleLoadParamsView

urlpatterns = patterns('',
    url(r'^$', login_required(PagemapView.as_view()), name='index'),
    url(r'^insert/$', login_required(InsertObjectView.as_view(
        model=Page,
        template_name="adm/pagemap/insert.html",
        page_header=_(u"Site Structure"),
        form_class=Form
    )), name='insert'),
    url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(
        model=Page,
        template_name="adm/pagemap/update.html",
        page_header=_(u"Site Structure"),
        form_class=Form
    )), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteObjectView.as_view(
        page_header=_(u"Site Structure"),
        model=Page
    )), name='delete'),
    url(r'^move/(?P<pk>\d+)/$', login_required(SortableTreeGridMoveView.as_view(
        model=Page
    )), name='move'),
    url(r'^load-module-params/$',
        login_required(PageModuleLoadParamsView.as_view()),
        name='load-module-params'),
)