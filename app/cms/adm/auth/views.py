# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import FormView, RedirectView
from django.shortcuts import redirect
from django.contrib.auth import login, logout

from forms import LoginForm


class LoginView(FormView):
    template_name = "adm/auth/login.html"
    form_class = LoginForm

    def get_initial(self):
        if 'next' in self.request.GET:
            return {
                'next': self.request.GET.get('next', '')
            }
        return {}

    def form_valid(self, form):
        data = form.cleaned_data
        user = form.get_user()
        login(self.request, user)
        if data['next']:
            return redirect(data['next'])
        else:
            return redirect('/')


class LogoutView(RedirectView):
    url = 'dashboard'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.url)
