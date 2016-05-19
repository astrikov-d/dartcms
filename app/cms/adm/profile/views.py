# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from forms import ProfileForm


class ProfileSettingsView(FormView):
    template_name = "adm/profile/index.html"
    form_class = ProfileForm
    success_url = reverse_lazy("profile:index", kwargs={'result': 'success'})

    def get_context_data(self, **kwargs):
        context = super(ProfileSettingsView, self).get_context_data(**kwargs)
        if 'result' in self.kwargs:
            context.update({
                'result': self.kwargs['result']
            })
        return context