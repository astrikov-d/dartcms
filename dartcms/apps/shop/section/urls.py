# coding: utf-8
from dartcms import get_model
from dartcms.utils.config import DartCMSConfig
from dartcms.views import DeleteObjectView, GridView, UpdateObjectView
from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.csrf import csrf_exempt

from .forms import ProductSectionForm
from .views import (AppendSectionView, GetTreeView, InsertSectionView,
                    MoveSectionView)

app_name='sections'

ProductSection = get_model('shop', 'ProductSection')

config = DartCMSConfig({
    'model': ProductSection,
    'parent_kwarg_name': 'catalog',
    'parent_model_fk': 'catalog_id',
    'grid': {
        'grid_columns': [
            {'field': 'name', 'width': '90%'},
            {'field': 'is_visible', 'width': '10%'},
        ],
        'template_name': 'dartcms/apps/shop/grid.html',
        'additional_grid_actions': [
            {'url': 'products', 'label': _('Products')}
        ]
    },
    'form': {
        'form_class': ProductSectionForm,
    },
})

insert_kwargs = config.form.copy()
insert_kwargs['template_name'] = 'dartcms/views/insert.html'

update_kwargs = config.form.copy()
update_kwargs['template_name'] = 'dartcms/views/update.html'

urlpatterns = [
    url(r'^$', GridView.as_view(**config.grid), name='index'),
    url(r'^get-tree/$', csrf_exempt(GetTreeView.as_view(**config.grid)), name='get_tree'),
    url(r'^insert/$', InsertSectionView.as_view(**insert_kwargs), name='insert'),
    url(r'^append/$', csrf_exempt(AppendSectionView.as_view()), name='append'),
    url(r'^move/$', csrf_exempt(MoveSectionView.as_view()), name='move'),
    url(r'^update/(?P<pk>\d+)/$', UpdateObjectView.as_view(**update_kwargs), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**config.base), name='delete'),
    url(r'^(?P<children_url>products)/(?P<section>\d+)/', include('dartcms.apps.shop.product.urls', namespace='products')),
]
