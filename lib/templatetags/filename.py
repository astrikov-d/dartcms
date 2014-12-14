__author__ = 'Dmitry Astrikov'

import os

from django import template

register = template.Library()

@register.filter
def filename(value):
    return os.path.basename(str(value))


@register.filter
def ext(value):
    name, extension = os.path.splitext(value.name.lower())
    return extension.replace('.','')
