# coding: utf-8
from dartcms.apps.auth.mixins import StaffRequiredMixin
from django.views.generic import TemplateView


class DashboardIndexView(StaffRequiredMixin, TemplateView):
    template_name = 'dartcms/apps/dashboard/index.html'
