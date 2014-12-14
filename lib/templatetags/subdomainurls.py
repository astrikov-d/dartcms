# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from urlparse import urlsplit, SplitResult

from django.template import Library
from django.conf import settings

from subdomains.compat.template import simple_tag
from subdomains.utils import reverse

register = Library()

UNSET = object()


def with_port(url_str):
    try:
        port = settings.PORT
    except AttributeError:
        port = None
    if port == 80:
        port = None
    url_split = urlsplit(url_str)
    if port:
        if not url_split.port and url_split.netloc:
            scheme, netloc, url, query, fragment = url_split
            netloc += ":%s" % port
            url_split = SplitResult(scheme, netloc, url, query, fragment)
    return url_split.geturl()


@simple_tag(register, takes_context=True)
def url(context, view, subdomain=UNSET, *args, **kwargs):
    if subdomain is UNSET:
        request = context.get('request')
        if request is not None:
            subdomain = getattr(request, 'subdomain', None)
        else:
            subdomain = None
    elif subdomain == '':
        subdomain = None

    return with_port(reverse(view, subdomain=subdomain, args=args, kwargs=kwargs))
