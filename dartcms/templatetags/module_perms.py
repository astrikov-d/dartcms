# coding: utf-8
from dartcms.apps.modules.models import ModulePermission
from django import template

try:
    import Image, ImageOps
except ImportError:
    from PIL import Image, ImageOps

register = template.Library()


#######################################################################################
# Module permissions.
# Usage:
# {% if module|has_permission:'CREATE %}
# ...
# {% endif %}
#######################################################################################
@register.simple_tag()
def check_module_permission(cms_module, user, permission_type):
    if user:
        perms = ModulePermission.objects.filter(user=user, module=cms_module).first()
        if perms:
            mapping = {
                'CREATE': 'can_insert',
                'UPDATE': 'can_update',
                'DELETE': 'can_delete',
            }
            return getattr(perms, mapping.get(permission_type))
    return False
