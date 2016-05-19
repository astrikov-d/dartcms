__author__ = 'Dmitry Astrikov'

from django import template

register = template.Library()

@register.filter
def lookup(d, key):
    return d[key]
