# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import TemplateView


class DashBoardIndex(TemplateView):
    template_name = "adm/dashboard/index.html"