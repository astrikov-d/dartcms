# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    next = forms.CharField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = self.cleaned_data
        if 'username' not in data or 'password' not in data:
            raise forms.ValidationError(u"Все поля обязательны для заполнения")

        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username,
                                password=password,
                                subdomain='admin')
            if user is None:
                raise forms.ValidationError("Неправильное имя пользователя или пароль")
            if not user.is_staff:
                raise forms.ValidationError("Доступ запрещен")
            self.user_cache = user
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
