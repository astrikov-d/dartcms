# -*- coding: utf-8 -*-

from django.forms import ModelForm, Select, DateInput, TextInput
from app.cms.models import SiteSettings


class SiteSettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        exclude = ['options', 'name', 'descr', 'type']
        widgets = {
            'date_value': DateInput(attrs={'class': 'date'}, format="%d.%m.%Y %H:%M:%S"),
        }

    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)

        label = self.instance.descr

        if self.instance.type == self.instance.DATE:
            del self.fields['text_value']
            del self.fields['file_value']
            self.fields['date_value'].label = label
        elif self.instance.type == self.instance.FILE:
            del self.fields['text_value']
            del self.fields['date_value']
            self.fields['file_value'].label = label
        else:
            del self.fields['file_value']
            del self.fields['date_value']
            self.fields['text_value'].label = label
            if self.instance.type == self.instance.RICH:
                self.fields['text_value'].widget.attrs = {'rows': 20, 'class': 'rte'}
            elif self.instance.type == self.instance.TEXT:
                self.fields['text_value'].widget = TextInput()
            elif self.instance.type == self.instance.SELECT:
                options = [(o, o) for o in self.instance.options.split(";")]
                self.fields['text_value'].widget = Select(choices=options)