# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import ListView, DetailView
from django.http import Http404

from models import Feed, FeedItem
from app.pagemap.models import Page


class FeedItemsListView(ListView):
    template_name = "site/feeds/list.html"
    paginate_by = 5

    def get_queryset(self):
        try:
            page = Page.objects.get(module__slug='feeds', slug=self.kwargs['page_slug'])
        except Page.DoesNotExist:
            raise Http404

        try:
            feed = Feed.objects.get(pk=page.module_params)
        except Feed.DoesNotExist:
            raise Http404

        return feed.feeditem_set.all()


class FeedItemDetailView(DetailView):
    model = FeedItem
    template_name = "site/feeds/detail.html"

    def get_object(self, queryset=None):
        try:
            return FeedItem.objects.get(pk=self.kwargs['pk'])
        except:
            raise Http404