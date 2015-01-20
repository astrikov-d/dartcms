# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.conf import settings
from django.contrib.sites.models import Site

from app.cms.models import SiteSettings


def template_variables(request):

    """
    This view returns list of global template variables
    """

    context = {}

    sitesettings = {}
    for s in SiteSettings.objects.all():
        sitesettings[s.name] = s.value

    context.update({
        'site': Site.objects.get_current(),
        'app_url': settings.APP_URL,
        'sitesettings': sitesettings
    })

    return context