# -*- coding: utf-8 -*-
from dartcms.utils.config import DartCMSConfig
from dartcms.utils.loading import get_model
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _

from .forms import PageForm
from .views import (AppendPageView, DeletePageView, GetTreeView,
                    InsertPageView, LoadModuleParamsView, MovePageView,
                    UpdatePageView, PageTreeView, OpenUrlRedirectView)

app_name = 'pages'

Page = get_model('pages', 'Page')

config = DartCMSConfig({
    'model': Page,
    'grid': {
        'grid_columns': [
            {'field': 'title', 'width': '60%'},
            {'field': 'url', 'width': '20%'},
            {'field': 'module', 'width': '20%'},
        ],
        'template_name': 'dartcms/apps/pages/grid.html',
        'search': [
            'title', 'url', 'module'
        ],
        'additional_grid_actions': [
            {'url': 'open_url', 'kwarg_name': 'pk', 'label': _('Open URL'), 'icon': 'chevron', 'target': '_blank'}
        ]
    },
    'form': {
        'form_class': PageForm,
        'tabs': True
    }
})

insert_kwargs = config.form.copy()
insert_kwargs['template_name'] = 'dartcms/apps/pages/insert.html'

update_kwargs = config.form.copy()
update_kwargs['template_name'] = 'dartcms/apps/pages/update.html'

delete_kwargs = config.base.copy()
delete_kwargs['template_name'] = 'dartcms/apps/pages/delete.html'

urlpatterns = [
    url(r'^$', PageTreeView.as_view(**config.grid), name='index'),
    url(r'^open_url/(?P<pk>\d+)/$', OpenUrlRedirectView.as_view(), name='open_url'),
    url(r'^get-tree/$', csrf_exempt(GetTreeView.as_view()), name='get_tree'),
    url(r'^insert/$', InsertPageView.as_view(**insert_kwargs), name='insert'),
    url(r'^append/$', csrf_exempt(AppendPageView.as_view()), name='append'),
    url(r'^move/$', csrf_exempt(MovePageView.as_view()), name='move'),
    url(r'^load-module-params/$', LoadModuleParamsView.as_view(), name='load_module_params'),
    url(r'^update/(?P<pk>\d+)/$', UpdatePageView.as_view(**update_kwargs), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeletePageView.as_view(**delete_kwargs), name='delete'),
]
