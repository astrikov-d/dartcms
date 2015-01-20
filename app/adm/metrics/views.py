# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import FormView
from django.conf import settings

from app.adm.api.clients.metrika import Client
from lib.views.adm.generic import ModulePermissionsMixin
from forms import MStatsForm


class ChangeSettings(ModulePermissionsMixin, FormView):
    form_class = MStatsForm
    template_name = "adm/metrics/index.html"

    def get_context_data(self, **kwargs):
        context = super(ChangeSettings, self).get_context_data(**kwargs)
        date_start = self.request.GET.get('date_start', '')
        date_end = self.request.GET.get('date_end', '')
        if date_start and date_end:
            traffic = Client().get_traffic(counter_id=settings.YM_COUNTER_ID, date_start=date_start, date_end=date_end)
        else:
            traffic = Client().get_traffic(counter_id=settings.YM_COUNTER_ID)
        context.update({
            'counter_exists': True,
            'traffic': traffic
        })
        return context

    def get_initial(self):
        return {
            'date_start': self.request.GET.get('date_start', ''),
            'date_end': self.request.GET.get('date_end', ''),
        }