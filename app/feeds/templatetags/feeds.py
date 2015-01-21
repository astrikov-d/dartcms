__author__ = 'Dmitry Astrikov'

from django import template

from app.pagemap.models import Page
from app.feeds.models import FeedItem


register = template.Library()

@register.filter
def get_page_slug_for_feeditem(item):
    feed = item.feed
    try:
        page = Page.objects.get(module__slug='feeds', module_params=feed.pk)
        return page.slug
    except Page.DoesNotExist:
        return None


@register.inclusion_tag('adm/feeds/dashboard/summary.html', takes_context=True)
def feeds_summary(context):
    return {
        'request': context['request'],
        'items_count': FeedItem.objects.all().count(),
    }