# -*- coding: utf-8 -*-
from django import template
from app.models import Page

register = template.Library()

@register.inclusion_tag('site/navigation/top.html', takes_context=True)
def get_top_navigation(context):
    return {
        'request': context['request'],
        'pages': Page.objects.select_related().filter(is_enabled=True, is_in_menu=True, parent_id=1)
    }

@register.inclusion_tag('site/navigation/breadcrumbs.html', takes_context=True)
def get_breadcrumbs(context):

    pages = []
    if context['request'].page is not None:
        page = context['request'].page.parent
        while page is not None:
            pages.append(page)
            page = page.parent
        return {
            'pages': pages,
            'current_page': context['request'].page
        }

@register.filter
def get_breadcrumbs_for_page(page):
    pages = []
    while page is not None:
        pages.append(page)
        page = page.parent
    return pages