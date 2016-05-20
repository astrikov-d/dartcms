# coding: utf-8
from dartcms.apps.modules.models import Module


def modules_data(request):
    if not request.is_ajax() and request.user.is_authenticated() and request.user.is_staff:
        modules = request.user.module_set.all()

        module_groups = [m.group for m in modules]
        module_groups_set = set(module_groups)
        active_module_slug = request.path.strip('/').split('/')[0]

        if active_module_slug != '':
            try:
                active_module = Module.objects.get(slug=active_module_slug)
            except Module.DoesNotExist:
                active_module = None
        else:
            active_module = None

        return {
            'module_groups': module_groups_set,
            'active_module': active_module
        }
    else:
        return {}
