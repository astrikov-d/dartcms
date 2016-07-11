# coding: utf-8
from django.views.generic import TemplateView

from dartcms.apps.auth.mixins import StaffRequiredMixin


class DashboardIndexView(StaffRequiredMixin, TemplateView):
    template_name = 'dartcms/apps/dashboard/index.html'
