# coding: utf-8
from django.forms import ModelForm

from .models import Folder


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']
