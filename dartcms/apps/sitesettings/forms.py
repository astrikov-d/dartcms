# coding: utf-8
from dartcms.apps.sitesettings.models import SiteSettings
from django.forms import ModelForm, Select, TextInput

FORM_MAP = {
    SiteSettings.OBJECT: ('object_id', ['text_value', 'file_value', 'boolean_value', 'date_value']),
    SiteSettings.BOOLEAN: ('boolean_value', ['text_value', 'file_value', 'object_id', 'date_value']),
    SiteSettings.DATE: ('date_value', ['text_value', 'file_value', 'object_id', 'boolean_value']),
    SiteSettings.FILE: ('file_value', ['text_value', 'date_value', 'object_id', 'boolean_value']),
    SiteSettings.TEXT: ('text_value', ['file_value', 'date_value', 'object_id', 'boolean_value'])
}


class SiteSettingsForm(ModelForm):
    class Meta:
        model = SiteSettings
        exclude = ['slug', 'description', 'type', 'options', 'content_type']

    def __init__(self, *args, **kwargs):
        super(SiteSettingsForm, self).__init__(*args, **kwargs)

        meta = getattr(self, 'Meta', None)
        exclude = getattr(meta, 'exclude', [])

        form_map = FORM_MAP.get(self.instance.type, FORM_MAP[SiteSettings.TEXT])
        self.fields[form_map[0]].label = self.instance.description
        exclude = exclude + form_map[1]

        if self.instance.type == self.instance.OBJECT:
            options = [(0, '---')] + [
                (choice.pk, choice) for choice in self.instance.content_type.model_class().objects.all()]
            self.fields['object_id'].widget = Select(choices=options)
        elif self.instance.type == self.instance.RICH:
            self.fields['text_value'].widget.attrs = {'class': 'rte'}
        elif self.instance.type == self.instance.TEXT:
            self.fields['text_value'].widget = TextInput()
        elif self.instance.type == self.instance.SELECT:
            options = [(o, o) for o in self.instance.options.split(";")]
            self.fields['text_value'].widget = Select(choices=options)

        for field_name in exclude:
            if field_name in self.fields:
                del self.fields[field_name]
