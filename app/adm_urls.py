# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.views.i18n import javascript_catalog

from app.cms.adm.dashboard.views import DashBoardIndex

admin.autodiscover()

js_info_dict = {
    'packages': ('app',),
}

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^secret/', include(admin.site.urls)),
    url(r'^$', login_required(DashBoardIndex.as_view()), name='dashboard'),
    url(r'^auth/', include('app.cms.adm.auth.urls')),
    url(r'^cms-users/', include('app.cms.adm.cmsusers.urls', namespace='cmsusers')),
    url(r'^site-settings/', include('app.cms.adm.sitesettings.urls', namespace='sitesettings')),
    url(r'^feeds/', include('app.feeds.adm.urls', namespace='feeds')),
    url(r'^products/', include('app.shop.adm.urls', namespace='shop')),
    url(r'^feedback/', include('app.feedback.adm.urls', namespace='feedback')),
    url(r'^pagemap/', include('app.pagemap.adm.urls', namespace='pagemap')),
    url(r'^metrics/', include('app.cms.adm.metrics.urls', namespace='metrics')),
    url(r'^filemanager/', include('app.cms.adm.filemanager.urls', namespace='filemanager')),
    url(r'^profile/', include('app.cms.adm.profile.urls', namespace='profile')),
    url(r'^', include('app.adv.adm.urls', namespace='adv')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )