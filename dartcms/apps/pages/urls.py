# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import GridView, UpdateObjectView, DeleteObjectView
from .forms import PageForm
from .views import GetTreeView, InsertPageView, AppendPageView, MovePageView

Page = get_model('pages', 'Page')

config = DartCMSConfig({
    'model': Page,
    'grid': {
        'grid_columns': (
            ('title', _('Title'), 'string', '60%'),
            ('url', _('URL'), 'datetime', '20%'),
            ('module', _('Page Module'), 'boolean', '20%'),
        ),
        'template_name': 'dartcms/apps/pages/grid.html'
    },
    'form': {
        'form_class': PageForm
    }
})

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^get-tree/$', csrf_exempt(GetTreeView.as_view(**config.grid)), name='get_tree'),
    url(r'^insert/$', InsertPageView.as_view(**config.form), name='insert'),
    url(r'^append/$', csrf_exempt(AppendPageView.as_view()), name='append'),
    url(r'^move/$', csrf_exempt(MovePageView.as_view()), name='move'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**config.form), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
