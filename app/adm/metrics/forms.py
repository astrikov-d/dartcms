# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms


class MStatsForm(forms.Form):

    date_start = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'date',
            'placeholder': 'Дата начала'
        }, format='%d.%m.%Y'),
        label='Дата начала'
    )

    date_end = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'date',
            'placeholder': 'Дата окончания'
        }, format='%d.%m.%Y'),
        label='Дата окончания'
    )