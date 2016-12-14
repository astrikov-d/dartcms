# -*- coding: utf-8 -*-
from datetime import datetime

from django import template

from dartcms.apps.ads.models import AdPlace
from dartcms.utils.loading import get_model

register = template.Library()


@register.inclusion_tag('dartcms/apps/ads/place.html', name='ad_place', takes_context=True)
def ad_place(context, place, limit=1):
    return get_ads(context, place, limit)


def get_ads(context, place, limit):
    if not hasattr(context['request'], 'page') or context['request'].page is None:
        return {}

    section = context['request'].page.ad_section
    place = AdPlace.objects.get(slug=place)

    ad_model = get_model('ads', 'Ad')

    ads = ad_model.objects.filter(
        section=section,
        place=place,
        date_from__lt=datetime.now(),
        date_to__gt=datetime.now()
    ).order_by('?')[0:limit]

    return {'object_list': ads}
