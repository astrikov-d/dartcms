# coding: utf-8
from django.conf.urls import include, url
from django.views.i18n import javascript_catalog

js_info_dict = {
    'packages': ('dartcms',),
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict, name='javascript-catalog'),

    url(r'^', include('dartcms.apps.dashboard.urls', namespace='dashboard')),
    url(r'^auth/', include('dartcms.apps.auth.urls', namespace='auth')),
    url(r'^cms-users/', include('dartcms.apps.users.urls', namespace='users')),
    url(r'^sitemap/', include('dartcms.apps.pages.urls', namespace='pages')),
]
