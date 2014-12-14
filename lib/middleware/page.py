# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from app.models import Page


class PageMiddleware(object):
    def process_request(self, request):
        path = u"/%s/" % request.path.strip('/')
        try:
            page = Page.objects.get(url=path)
            request.page = page
        except Page.DoesNotExist:
            path_parts = request.path.strip('/').split('/')
            while path_parts:
                path_parts.pop()
                if path_parts:
                    path = "/%s/" % "/".join(path_parts)
                    try:
                        page = Page.objects.get(url=path)
                        request.page = page
                        break
                    except Page.DoesNotExist:
                        continue
