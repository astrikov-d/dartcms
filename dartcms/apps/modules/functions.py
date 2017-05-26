# coding: utf-8
from django.core.urlresolvers import NoReverseMatch, reverse

from .models import Module, ModulePermission


def get_current_module(path):
    try:
        dartcms_path = reverse('dartcms:dashboard:index')
    except NoReverseMatch:
        return {}

    module_slug = path.replace(dartcms_path, '', 1).split('/')[0]
    if module_slug:
        try:
            return Module.objects.get(slug=module_slug)
        except Module.DoesNotExist:
            pass


def get_current_module_perms(request):
    cms_module = get_current_module(request.path)
    if cms_module:
        return ModulePermission.objects.filter(user=request.user, module=cms_module).first()
