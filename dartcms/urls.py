# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.views.i18n import JavaScriptCatalog

js_info_dict = {
    'packages': ('dartcms',),
}

app_name = 'dartcms'

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', JavaScriptCatalog.as_view(), name='javascript-catalog'),

    url(r'^', include('dartcms.apps.dashboard.urls', namespace='dashboard')),
    url(r'^auth/', include('dartcms.apps.auth.urls', namespace='auth')),

    url(r'^filemanager/', include('dartcms.apps.filemanager.urls', namespace='filemanager')),
    url(r'^dict-(?P<module_slug>[a-z_-]{3,50})/',
        include('dartcms.apps.dicts.urls', namespace='dicts')),
]

if 'dartcms.apps.users.groups' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^user-groups/', include('dartcms.apps.users.groups.urls', namespace='user_groups')), ]

if 'dartcms.apps.siteusers' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^site-users/', include('dartcms.apps.siteusers.urls', namespace='siteusers')), ]

if 'dartcms.apps.users' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^cms-users/', include('dartcms.apps.users.urls', namespace='users')), ]

if 'dartcms.apps.pages' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^sitemap/', include('dartcms.apps.pages.urls', namespace='pages')), ]

if 'dartcms.apps.feeds' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^feeds/', include('dartcms.apps.feeds.urls', namespace='feeds')), ]

if 'dartcms.apps.sitesettings' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^sitesettings/', include('dartcms.apps.sitesettings.urls', namespace='sitesettings')), ]

if 'dartcms.apps.ads' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^ad/', include('dartcms.apps.ads.ad.urls', namespace='ad')),
        url(r'^adplace/', include('dartcms.apps.ads.adplace.urls', namespace='adplace')),
        url(r'^adsection/', include('dartcms.apps.ads.adsection.urls', namespace='adsection')), ]

if 'dartcms.apps.feedback' in settings.INSTALLED_APPS:
    urlpatterns += [url(r'^feedback/', include('dartcms.apps.feedback.urls', namespace='feedback')), ]

if 'dartcms.apps.shop' in settings.INSTALLED_APPS:
    urlpatterns += [
        url(r'^shop-catalog/', include('dartcms.apps.shop.catalog.urls', namespace='shop-catalog')),
        url(r'^shop-orders/', include('dartcms.apps.shop.order.urls', namespace='shop-orders')), ]

additional_apps = getattr(settings, 'DARTCMS_ADDITIONAL_APPS_URLPATTERNS', [])

if additional_apps:
    additional_patterns = []
    for app in additional_apps:
        additional_patterns.append(url(r'^%s/' % app[0], include(app[1], namespace=app[2])))

    urlpatterns += additional_patterns
