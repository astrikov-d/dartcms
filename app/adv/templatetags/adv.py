# -*- coding: utf-8 -*-
from datetime import datetime
from django import template

from app.adv.models import Adv, AdvPlace

register = template.Library()

@register.inclusion_tag('site/adv/banner.html', name='banner_place', takes_context=True)
def banner_place(context, adv_place, limit=1):
    return get_banners(context, adv_place, limit)


def get_banners(context, adv_place, limit):

    if not hasattr(context['request'], 'page') or context['request'].page is None:
        return {}

    section = context['request'].page.adv_section
    place = AdvPlace.objects.get(slug=adv_place)
    banners = Adv.objects.filter(
        section=section,
        place=place,
        date_from__lt=datetime.now(),
        date_to__gt=datetime.now()
    ).order_by('?')[0:limit]

    if banners:
        banner = banners[0]
    else:
        banner = None

    return {
        'object': banner
    }