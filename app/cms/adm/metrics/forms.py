# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django import forms
from django.utils.translation import ugettext_lazy as _


class MStatsForm(forms.Form):

    date_start = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'date',
            'placeholder': _(u'Date of Start')
        }, format='%d.%m.%Y'),
        label=_(u'Date of Start')
    )

    date_end = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'date',
            'placeholder':  _(u'Date of End')
        }, format='%d.%m.%Y'),
        label=_(u'Date of End')
    )