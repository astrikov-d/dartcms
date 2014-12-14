# -*- coding: utf-8 -*-
from datetime import datetime
from django import template
from app.adv.models import Adv
from app.adv.models import AdvPlace

register = template.Library()

@register.inclusion_tag('adv/site/banners.html', name='banner_place', takes_context=True)
def banner_place(context):
    return get_banners(context, 'banner_place', 4)


def get_banners(context, adv_place, limit=1):
    if 'request' in context and context['request'].page is not None:
        return {}
    section = context['request'].page.adv_section
    place = AdvPlace.objects.get(slug=adv_place)
    banners = Adv.objects.filter(
        section=section,
        place=place,
        date_from__lt=datetime.now(),
        date_to__gt=datetime.now()
    ).order_by('?')[0:limit]
    return {
        'banners': banners
    }