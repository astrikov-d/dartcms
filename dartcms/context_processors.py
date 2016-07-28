# coding: utf-8
from django.core.urlresolvers import reverse, NoReverseMatch


def modules_data(request):
    try:
        dartcms_path = reverse('dartcms:dashboard:index')
    except NoReverseMatch:
        return {}

    if not request.is_ajax() and request.user.is_authenticated() and request.user.is_staff:
        modules = request.user.module_set.all()

        module_groups = [m.group for m in modules]
        module_groups_set = set(module_groups)

        res = dict(module_groups=module_groups_set)

        active_module_slug = request.path.replace(dartcms_path, '', 1).split('/')[0]
        if active_module_slug:
            module = modules.filter(slug=active_module_slug).last()
            if module:
                res.update(
                    dict(active_module_slug=active_module_slug,
                         active_group_slug=module.group.slug)
                )
        return res
    else:
        return {}
