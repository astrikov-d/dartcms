# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import os

def template_variables(request):

    """
    This view returns list of global template variables
    """

    from django.conf import settings

    if not request.is_ajax() and request.user.is_authenticated():

        from app.models import CMSModuleGroup, CMSModule

        cms_module_groups = CMSModuleGroup.objects.select_related().all()
        active_module_slug = request.path.strip("/").split("/")[0]
        if active_module_slug != "":
            try:
                active_module = CMSModule.objects.get(slug=active_module_slug)
            except CMSModule.DoesNotExist:
                active_module = None
        else:
            active_module = None

        return {
            'cms_module_groups': cms_module_groups,
            'active_module': active_module
        }
    else:
        return {}