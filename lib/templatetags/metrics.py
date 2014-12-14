__author__ = 'Dmitry Astrikov'

import time
import datetime

from django import template

register = template.Library()

@register.filter
def ymdate(value):
    return datetime.datetime.strptime(value, "%Y%m%d")
