# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import ListView, TemplateView

from app.models import Project


class HomepageView(TemplateView):
    template_name = "site/homepage/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context.update({
            'own_projects': Project.objects.filter(project_type__slug='own')
        })
        return context
