# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from dartcms.views import DeleteObjectView, GridView, UpdateObjectView

from .forms import PageForm
from .views import (AppendPageView, GetTreeView, InsertPageView,
                    LoadModuleParamsView, MovePageView)

Page = get_model('pages', 'Page')

config = DartCMSConfig({
    'model': Page,
    'grid': {
        'grid_columns': [
            {'field': 'title', 'width': '60%'},
            {'field': 'url', 'width': '20%'},
            {'field': 'module', 'width': '20%'},
        ],
        'template_name': 'dartcms/apps/pages/grid.html'
    },
    'form': {
        'form_class': PageForm,
    }
})

insert_kwargs = config.form.copy()
insert_kwargs['template_name'] = 'dartcms/apps/pages/insert.html'

update_kwargs = config.form.copy()
update_kwargs['template_name'] = 'dartcms/apps/pages/update.html'

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^get-tree/$', csrf_exempt(GetTreeView.as_view(**config.grid)), name='get_tree'),
    url(r'^insert/$', InsertPageView.as_view(**insert_kwargs), name='insert'),
    url(r'^append/$', csrf_exempt(AppendPageView.as_view()), name='append'),
    url(r'^move/$', csrf_exempt(MovePageView.as_view()), name='move'),
    url(r'^load-module-params/$', LoadModuleParamsView.as_view(), name='load_module_params'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**update_kwargs), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
]
