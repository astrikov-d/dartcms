# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static

from app.site.homepage.views import HomepageView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^page/', include('app.site.pagemap.urls', namespace="page")),
    url(r'^feeds/', include('app.site.feeds.urls', namespace="feeds")),
    #url(r'^photos/', include('app.site.gallery.urls', namespace="gallery")),
    url(r'^feedback/', include('app.site.feedback.urls', namespace="feedback")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )