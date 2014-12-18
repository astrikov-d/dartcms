# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms

from app.models import FeedbackMessage


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackMessage
        exclude = ['date_created', 'answer', 'is_visible', 'date_published', 'feedback_type']