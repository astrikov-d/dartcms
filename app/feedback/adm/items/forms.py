# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms
from django.utils.translation import ugettext_lazy as _

from app.feedback.models import FeedbackMessage


class Form(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        exclude = ['feedback_type']
        widgets = {
            'answer': forms.Textarea(attrs={'class': 'rte'}),
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