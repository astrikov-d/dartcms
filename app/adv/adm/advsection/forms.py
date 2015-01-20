# -*- coding: utf-8 -*-

from django.forms import ModelForm
from app.adv.models import AdvSection


class Form(ModelForm):
    class Meta:
        model = AdvSection