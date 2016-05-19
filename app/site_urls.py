# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.conf.urls import patterns, url, include
from django.conf.urls.static import static
from django.http import HttpResponse

from app.homepage.views import HomepageView

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^page/', include('app.pagemap.urls', namespace="page")),
    url(r'^feeds/', include('app.feeds.urls', namespace="feeds")),
    url(r'^feedback/', include('app.feedback.urls', namespace="feedback")),
    url(r'^robots.txt$', lambda r: HttpResponse("User-agent: *\nDisallow:", mimetype="text/plain"))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
    )