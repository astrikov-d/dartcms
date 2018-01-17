# coding: utf-8
from django import forms

from .models import SiteUser


class UserForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'groups', 'is_staff', 'is_superuser')
