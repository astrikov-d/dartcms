# coding: utf-8
from django.conf import settings
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
    url(r'^feeds/', include('dartcms.apps.feeds.urls', namespace='feeds')),
    url(r'^filemanager/', include('dartcms.apps.filemanager.urls', namespace='filemanager')),
    url(r'^sitesettings/', include('dartcms.apps.sitesettings.urls', namespace='sitesettings')),
    url(r'^ad/', include('dartcms.apps.ads.ad.urls', namespace='ad')),
    url(r'^adplace/', include('dartcms.apps.ads.adplace.urls', namespace='adplace')),
    url(r'^adsection/', include('dartcms.apps.ads.adsection.urls', namespace='adsection')),
    url(r'^feedback/', include('dartcms.apps.feedback.urls', namespace='feedback')),
    url(r'^shop-catalog/', include('dartcms.apps.shop.catalog.urls', namespace='shop-catalog')),
    url(r'^shop-manufactures/', include('dartcms.apps.shop.manufacturer.urls', namespace='shop-manufacturers')),
    url(r'^shop-labels/', include('dartcms.apps.shop.label.urls', namespace='shop-labels')),
    url(r'^shop-orders/', include('dartcms.apps.shop.order.urls', namespace='shop-orders'))
]

additional_apps = getattr(settings, 'DARTCMS_ADDITIONAL_APPS_URLPATTERNS', [])

if additional_apps:
    additional_patterns = []
    for app in additional_apps:
        additional_patterns.append(url(r'^%s/' % app[0], include(app[1], namespace=app[2])))

    urlpatterns += additional_patterns
