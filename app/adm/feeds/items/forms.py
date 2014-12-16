# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms
from django.utils.translation import ugettext_lazy as _

from app.models import FeedItem


class Form(forms.ModelForm):
    class Meta:
        model = FeedItem
        exclude = ['feed', 'slug']
        widgets = {
            'short_text': forms.Textarea(attrs={'class': 'rte'}),
            'full_text': forms.Textarea(attrs={'class': 'rte'}),
        }

    date_published = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime'
            }
        ),
        input_formats=["%d.%m.%Y %H:%M:%S"],
        label=_(u'Date of publication')
    )