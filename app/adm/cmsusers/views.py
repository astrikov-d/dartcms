# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import FormView
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect

from lib.views.adm.generic import AdminMixin


class ChangePasswordView(AdminMixin, FormView):
    form_class = AdminPasswordChangeForm
    page_header = u'Пользователи'
    template_name = "adm/base/generic/change_password.html"

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs.update({
            'user': User.objects.get(pk=self.kwargs['pk'])
        })
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect("cmsusers:index")