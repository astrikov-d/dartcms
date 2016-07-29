# coding: utf-8
from django.core.urlresolvers import reverse, NoReverseMatch

from .models import Module


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