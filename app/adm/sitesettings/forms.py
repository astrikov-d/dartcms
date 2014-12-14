# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms

from app.models import SiteSettings


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings

    footer_content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'rte'
        }),
        label='Содержимое футера',
        required=False
    )