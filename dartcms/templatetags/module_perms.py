# coding: utf-8
from django import template

from dartcms.apps.modules.models import ModulePermission

try:
    import Image, ImageOps
except ImportError:
    from PIL import Image, ImageOps

register = template.Library()


#######################################################################################
# Module permissions.                                                           #
# Usage:                                                                              #
# {% if module|has_permission:'CREATE %}                                                        #
# ...                                                                                 #
# {% endif %}                                                               #
#######################################################################################
@register.simple_tag(takes_context=True)
def check_module_permission(context, cms_module, permission_type):
    perms = ModulePermission.objects.filter(user=context['request'].user, module=cms_module).first()
    if perms:
        mapping = {
            'CREATE': 'can_insert',
            'UPDATE': 'can_update',
            'DELETE': 'can_delete',
        }
        return getattr(perms, mapping.get(permission_type))
    return False