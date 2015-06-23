__author__ = 'astrikovd'

from django import template
from django.conf import settings

from app.pagemap.models import Page
from app.cms.adm.api.clients.metrika import Client


register = template.Library()

@register.inclusion_tag('adm/metrics/dashboard/summary.html', takes_context=True)
def traffic_summary(context):
    traffic = Client().get_traffic(counter_id=settings.YM_COUNTER_ID)
    traffic = list(reversed(traffic['data']))
    if len(traffic) > 0:
        stat = traffic[0]
    return {
        'request': context['request'],
        'stat': stat,
    }
