# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

BOOLEAN_CHOICES = (
    ('', ''),
    ('ON', _('Yes')),
    ('OFF', _('No'))
)

DYNAMIC_FIELDS_MAPPING = {
    'STRING': {'class': forms.CharField, 'defaults': {'max_length': 255}},
    'DATE': {'class': forms.DateField, 'defaults': {'widget': forms.TextInput(attrs={'class': 'date'})}},
    'TIME': {'class': forms.TimeField, 'defaults': {'widget': forms.TextInput(attrs={'class': 'time'})}},
    'DATETIME': {'class': forms.DateTimeField, 'defaults': {'widget': forms.TextInput(attrs={'class': 'datetime'})}},
    'FOREIGN_KEY': {'class': forms.ModelChoiceField},
    'BOOLEAN': {'class': forms.CharField,
                'defaults': {'widget': forms.Select(choices=BOOLEAN_CHOICES)}}
}


class DynamicFieldsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra', [])

        super(DynamicFieldsForm, self).__init__(*args, **kwargs)

        for item in extra:
            field = DYNAMIC_FIELDS_MAPPING.get(item['type'], DYNAMIC_FIELDS_MAPPING['STRING'])
            if 'defaults' in field:
                defaults = field['defaults'].copy()
                defaults.update(item['kwargs'])
            else:
                defaults = item['kwargs']

            if item['type'] in ('DATE', 'TIME', 'DATETIME'):
                label = defaults['label']
                for suffix in ('from', 'to'):
                    defaults['label'] = '%s (%s)' % (label, _('from') if suffix == 'from' else _('to'))
                    self.fields['%s_%s' % (item['field'], suffix)] = field['class'](**defaults)
            else:
                self.fields[item['field']] = field['class'](**defaults)
