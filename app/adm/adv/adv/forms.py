# -*- coding: utf-8 -*-

from django.forms import ModelForm, DateTimeInput
from app.models import Adv


class Form(ModelForm):
    class Meta:
        model = Adv
        widgets = {
            'date_from': DateTimeInput(attrs={'class': 'datetime'}),
            'date_to': DateTimeInput(attrs={'class': 'datetime'}),
        }