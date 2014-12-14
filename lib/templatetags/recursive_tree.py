# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import template

register = template.Library()


@register.inclusion_tag('adm/lists/recursive_tree/children.html', takes_context=True)
def recursive_tree(context):
    return context