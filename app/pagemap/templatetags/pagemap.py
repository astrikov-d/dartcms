__author__ = 'astrikovd'

from django import template
from app.pagemap.models import Page

register = template.Library()

@register.inclusion_tag('adm/pagemap/dashboard/summary.html', takes_context=True)
def page_summary(context):
    return {
        'request': context['request'],
        'pages_count': Page.objects.all().count(),
    }
