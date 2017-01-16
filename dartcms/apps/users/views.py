# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView

from dartcms.apps.auth.utils import get_user_model
from dartcms.views import AdminMixin, InsertObjectView, UpdateObjectView


class ChangePasswordView(AdminMixin, FormView):
    form_class = AdminPasswordChangeForm
    page_header = _('Users')
    template_name = 'dartcms/apps/users/change_password.html'
    success_url = reverse_lazy('dartcms:users:index')

    @property
    def user_model(self):
        return get_user_model()

    def get_form_kwargs(self):
        kwargs = super(ChangePasswordView, self).get_form_kwargs()
        kwargs['user'] = self.user_model.objects.get(pk=self.kwargs['pk'])
        return kwargs

    def get_context_data(self, *args, **kwargs):
        context = super(ChangePasswordView, self).get_context_data(**kwargs)
        context['index_url'] = reverse_lazy('dartcms:users:index')
        return context

    def form_valid(self, form):
        form.save()
        return super(ChangePasswordView, self).form_valid(form)


class SaveUserMixin(object):
    def form_valid(self, form):
        data = form.cleaned_data
        user = form.save()
        if user.id:
            user.module_set.clear()
            user.user_groups.clear()

        for module in data.get('modules', []):
            user.module_set.add(module)

        for group in data.get('user_groups', []):
            user.user_groups.add(group)

        return self.render_to_json_response({'result': True, 'action': self.action})


class CMSUserUpdateView(SaveUserMixin, UpdateObjectView):
    success_url = reverse_lazy('dartcms:users:index')
    action = 'UPDATE'

    def get_initial(self):
        obj = self.get_object()
        return {
            'modules': obj.module_set.all(),
            'user_groups': obj.user_groups.all()
        }


class CMSUserInsertView(SaveUserMixin, InsertObjectView):
    action = 'INSERT'

    def get_success_url(self):
        return reverse_lazy('dartcms:users:change_password', kwargs={'pk': self.object.pk})
