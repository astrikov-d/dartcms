# coding: utf-8
from dartcms.apps.modules.models import Module
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import CMSUser, UserGroup


class UserForm(forms.ModelForm):
    class Meta:
        model = CMSUser
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'groups', 'is_staff')

    modules = forms.ModelMultipleChoiceField(required=False, label=_('Modules'),
                                             queryset=Module.objects.all())
    user_groups = forms.ModelMultipleChoiceField(required=False, label=_('Groups'),
                                                 queryset=UserGroup.objects.all())
