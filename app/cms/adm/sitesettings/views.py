# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView
from django.shortcuts import redirect

from app.cms.models import SiteSettings
from forms import SiteSettingsForm


class SiteSettingsUpdateView(UpdateView):
    template_name = "adm/sitesettings/index.html"
    form_class = SiteSettingsForm
    success_url = reverse_lazy("sitesettings:index", kwargs={'result': 'success'})

    def get_context_data(self, **kwargs):
        context = super(SiteSettingsUpdateView, self).get_context_data(**kwargs)
        if 'result' in self.kwargs:
            context.update({
                'result': self.kwargs['result']
            })
        return context

    def get_object(self, queryset=None):
        try:
            return SiteSettings.objects.first()
        except SiteSettings.DoesNotExist:
            # Initial site settings
            settings = SiteSettings()
            settings.save()
            return settings