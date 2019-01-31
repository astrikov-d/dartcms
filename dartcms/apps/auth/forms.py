# coding: utf-8
from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(label=User._meta.get_field(User.USERNAME_FIELD).verbose_name.title())
    password = forms.CharField(widget=forms.PasswordInput, label=_('Password'))
    next = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        if 'username' not in data or 'password' not in data:
            raise forms.ValidationError(_('All fields are required'))

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,
                                password=password)
            if user is None:
                raise forms.ValidationError(_('Incorrect username of password'))
            if not user.is_staff:
                raise forms.ValidationError(_('Access denied'))

            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
