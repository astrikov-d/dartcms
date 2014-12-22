# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.i18n import javascript_catalog

from app.adm.dashboard.views import DashBoardIndex

admin.autodiscover()

js_info_dict = {
    'packages': ('app',),
}

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^secret/', include(admin.site.urls)),
    url(r'^$', login_required(DashBoardIndex.as_view()), name='dashboard'),
    url(r'^auth/', include('app.adm.auth.urls')),
    url(r'^cms-users/', include('app.adm.cmsusers.urls', namespace='cmsusers')),
    url(r'^site-settings/', include('app.adm.sitesettings.urls', namespace='sitesettings')),
    url(r'^feeds/', include('app.adm.feeds.urls', namespace='feeds')),
    url(r'^products/', include('app.adm.shop.urls', namespace='shop')),
    url(r'^feedback/', include('app.adm.feedback.urls', namespace='feedback')),
    url(r'^pagemap/', include('app.adm.pagemap.urls', namespace='pagemap')),
    url(r'^metrics/', include('app.adm.metrics.urls', namespace='metrics')),
    url(r'^filemanager/', include('app.adm.filemanager.urls', namespace='filemanager')),
    url(r'^profile/', include('app.adm.profile.urls', namespace='profile')),
    url(r'^', include('app.adm.adv.urls', namespace='adv')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )