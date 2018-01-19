# -*- coding: utf-8 -*-
from dartcms.apps.auth.utils import get_user_model
from dartcms.apps.modules.models import Module, ModuleGroup, ModulePermission
from dartcms.views import AdminMixin, InsertObjectView, UpdateObjectView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView


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
        context['index_url'] = self.success_url
        return context

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        return super(ChangePasswordView, self).form_valid(form)


class SaveUserMixin(object):
    def set_module_permissions(self, user):
        read = self.request.POST.getlist('read')
        insert = self.request.POST.getlist('insert')
        update = self.request.POST.getlist('update')
        delete = self.request.POST.getlist('delete')

        for module_id in read:
            user.module_set.add(Module.objects.get(pk=module_id))
            kwargs = {
                'can_insert': module_id in insert,
                'can_update': module_id in update,
                'can_delete': module_id in delete,
                'user_id': user.id,
                'module_id': module_id
            }
            ModulePermission.objects.create(**kwargs)

    def form_valid(self, form):
        data = form.cleaned_data
        user = form.save()
        if user.id:
            user.module_set.clear()
            user.user_module_permissions.all().delete()
            user.user_groups.clear()

        for group in data.get('user_groups', []):
            user.user_groups.add(group)

        self.set_module_permissions(user)

        return self.render_to_json_response({'result': True, 'action': self.action})


class ModulesContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ModulesContextMixin, self).get_context_data(**kwargs)
        context['module_groups'] = ModuleGroup.objects.all()
        return context


class CMSUserUpdateView(SaveUserMixin, ModulesContextMixin, UpdateObjectView):
    action = 'UPDATE'
    success_url = reverse_lazy('dartcms:users:index')
    template_name = 'dartcms/apps/users/update.html'

    def get_initial(self):
        obj = self.get_object()
        return {
            'user_groups': obj.user_groups.all()
        }


class CMSUserInsertView(SaveUserMixin, ModulesContextMixin, InsertObjectView):
    template_name = 'dartcms/apps/users/insert.html'
    action = 'INSERT'

    def get_success_url(self):
        return reverse_lazy('dartcms:users:change_password', kwargs={'pk': self.object.pk})
