# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from app.cms.models import SiteSettings
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import GridView, UpdateObjectView
from forms import SiteSettingsForm as Form

kwargs = {
    'model': SiteSettings,
    'form_class': Form,
    'grid_columns': (
        ('descr', _(u'Name'), 'string', '20%'),
        ('type_display', _(u'Type'), 'string', '20%'),
        ('value_for_grid', _(u'Value'), 'string', '60%'),
    ),
    'allow_insert': False,
    'allow_delete': False
}

urlpatterns = patterns('',
   url(r'^$', login_required(GridView.as_view(**kwargs)), name='index'),
   url(r'^page/(?P<page>\d+)/$', login_required(GridView.as_view(**kwargs)), name='index'),
   url(r'^update/(?P<pk>\d+)/$', login_required(UpdateObjectView.as_view(**kwargs)), name='update'),
)