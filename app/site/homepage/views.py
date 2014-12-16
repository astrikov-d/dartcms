# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import ListView, TemplateView


class HomepageView(TemplateView):
    template_name = "site/homepage/index.html"

