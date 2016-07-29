# coding: utf-8
from dartcms.apps.modules.functions import get_current_module


def modules_data(request):
    if not request.is_ajax() and request.user.is_authenticated() and request.user.is_staff:
        modules = request.user.module_set.all()

        module_groups = [m.group for m in modules]
        module_groups_set = set(module_groups)

        res = dict(module_groups=module_groups_set)

        module = get_current_module(request.path)
        if module:
            res.update(
                dict(active_module_slug=module.slug,
                     active_group_slug=module.group.slug)
            )
        return res
    else:
        return {}
