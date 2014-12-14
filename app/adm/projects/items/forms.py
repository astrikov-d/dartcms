# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms

from app.models import Project


class Form(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['project_type', 'slug']

    short_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'rte'
        }),
        label='Анонс'
    )

    full_text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'rte'
        }),
        label='Полный текст'
    )

    date_published = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime'
            }
        ),
        input_formats=["%d.%m.%Y %H:%M:%S"],
        label='Дата публикации'
    )