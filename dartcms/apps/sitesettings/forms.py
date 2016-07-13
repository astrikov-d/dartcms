# coding: utf-8
from django.forms import DateTimeInput, ModelForm, Select, TextInput

from dartcms.apps.sitesettings.models import SiteSettings


class SiteSettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        exclude = ['slug', 'description', 'type', 'options']

    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)

        label = self.instance.description

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
                self.fields['text_value'].widget.attrs = {'class': 'rte'}
            elif self.instance.type == self.instance.TEXT:
                self.fields['text_value'].widget = TextInput()
            elif self.instance.type == self.instance.SELECT:
                options = [(o, o) for o in self.instance.options.split(";")]
                self.fields['text_value'].widget = Select(choices=options)
