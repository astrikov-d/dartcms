# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib import admin

from app.adm.dashboard.views import DashBoardIndex

admin.autodiscover()

#handler404 = 'app.admin.pages.views.error404'

urlpatterns = patterns('',
    url(r'^secret/', include(admin.site.urls)),
    url(r'^$', login_required(DashBoardIndex.as_view()), name='dashboard'),
    url(r'^auth/', include('app.adm.auth.urls')),
    url(r'^cms-users/', include('app.adm.cmsusers.urls', namespace='cmsusers')),
    url(r'^site-settings/', include('app.adm.sitesettings.urls', namespace='sitesettings')),
    url(r'^feeds/', include('app.adm.feeds.urls', namespace='feeds')),
    url(r'^projects/', include('app.adm.projects.urls', namespace='projects')),
    url(r'^pagemap/', include('app.adm.pagemap.urls', namespace='pagemap')),
    url(r'^metrics/', include('app.adm.metrics.urls', namespace='metrics')),
    url(r'^filemanager/', include('app.adm.filemanager.urls', namespace='filemanager')),
    url(r'^', include('app.adm.adv.urls', namespace='adv')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )