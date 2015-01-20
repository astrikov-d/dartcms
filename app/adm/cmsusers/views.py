# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.views.generic import FormView
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _

from lib.views.adm.generic import AdminMixin, UpdateObjectView


class ChangePasswordView(AdminMixin, FormView):
    form_class = AdminPasswordChangeForm
    page_header = _(u'Users')
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


class CMSUserUpdateView(UpdateObjectView):
    success_url = "cmsusers:index"

    def get_initial(self):
        obj = self.get_object()
        return {
            'modules': obj.cmsmodule_set.all()
        }