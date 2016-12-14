# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from dartcms.apps.modules.models import Module

from .models import UserGroup


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'groups')

    modules = forms.ModelMultipleChoiceField(label=_('Modules'), queryset=Module.objects.all())
    user_groups = forms.ModelMultipleChoiceField(label=_('Groups'), queryset=UserGroup.objects.all())
