__author__ = 'Dmitry Astrikov'

from django import template

register = template.Library()

@register.filter
def splitlines(string):
    return string.splitlines()

@register.filter
def intvalue(string):
    return int(float(string))

@register.filter
def stringvalue(string):
    return str(string)

@register.filter
def floatvalue(string):
    return float(string)

@register.filter
def floatdot(value):
    return str(value).replace(",",".")

@register.filter
def split(value, needle):
    return value.split(needle)