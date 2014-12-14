# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from django.db.models import Q
from django.forms import ModelForm, ValidationError

from app.models import Folder, File


class FolderForm(ModelForm):
    class Meta:
        model = Folder
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FolderForm, self).__init__(*args, **kwargs)

    def validate_unique(self):
        try:
            name = self.cleaned_data['name']
            if self.instance.pk:
                Folder.objects.get(~Q(id=self.instance.pk), name=name)
            else:
                Folder.objects.get(name=name)
            self._errors['name'] = ["Folder with that name already exists"]
            return super(FolderForm, self).validate_unique()
        except Folder.DoesNotExist:
            return super(FolderForm, self).validate_unique()


class FileUploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['path']