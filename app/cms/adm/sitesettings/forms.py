# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms

from app.cms.models import SiteSettings


class SiteSettingsForm(forms.ModelForm):
    class Meta:
        model = SiteSettings
        widgets = {
            'footer_content': forms.Textarea(attrs={'class': 'rte'})
        }