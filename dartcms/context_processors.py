# coding: utf-8
def modules_data(request):
    if not request.is_ajax() and request.user.is_authenticated() and request.user.is_staff:
        modules = request.user.module_set.all()

        module_groups = [m.group for m in modules]
        module_groups_set = set(module_groups)

        return {
            'module_groups': module_groups_set
        }
    else:
        return {}
