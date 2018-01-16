# coding: utf-8
from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from .forms import LoginForm


class LoginView(FormView):
    template_name = "dartcms/apps/auth/login.html"
    form_class = LoginForm

    def get_initial(self):
        if 'next' in self.request.GET:
            return {'next': self.request.GET['next']}
        return {}

    def form_valid(self, form):
        data = form.cleaned_data
        user = form.get_user()
        login(self.request, user)

        redirect_url = data.get('next', reverse_lazy('dartcms:dashboard:index'))
        return redirect(redirect_url)


class LogoutView(RedirectView):
    url = 'dartcms:dashboard:index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect(self.url)
