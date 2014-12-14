__author__ = 'Dmitry Astrikov'

from django import template

register = template.Library()

@register.filter
def key(d, key):
    if d:
        if key in d:
            return d[key]
        else:
            return False
    else:
        return False

