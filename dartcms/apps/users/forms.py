# coding: utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from dartcms.apps.modules.models import Module


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'groups', 'user_permissions')

    modules = forms.ModelMultipleChoiceField(label=_(u"Modules"), queryset=Module.objects.all())
