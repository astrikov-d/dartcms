# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

from dartcms.apps.auth.utils import get_user_model
from dartcms.apps.modules.models import Module

from .models import UserGroup


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'groups')

    modules = forms.ModelMultipleChoiceField(required=False, label=_('Modules'),
                                             queryset=Module.objects.all())
    user_groups = forms.ModelMultipleChoiceField(required=False, label=_('Groups'),
                                                 queryset=UserGroup.objects.all())
