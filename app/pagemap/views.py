# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import TemplateView
from django.http import Http404

from models import Page


class PageDetailView(TemplateView):
    template_name = "site/page/detail.html"

    def get_context_data(self, **kwargs):

        try:
            page = Page.objects.get(module__slug='pagemap', slug=self.kwargs['slug'])

        except Page.DoesNotExist:
            raise Http404

        context = super(PageDetailView, self).get_context_data(**kwargs)
        context.update({
            'page': page
        })
        return context