# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


from django import template

register = template.Library()

@register.filter
def attribute(obj, attribute_name):
    """
    Get object attribute.
    """
    return getattr(obj, attribute_name, None)