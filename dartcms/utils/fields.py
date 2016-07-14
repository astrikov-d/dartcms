from django import forms
from django.db.models import TextField


class RteField(TextField):
    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length, 'widget': forms.Textarea(attrs={'rows': 20, 'class': 'rte'})}
        defaults.update(kwargs)
        return super(RteField, self).formfield(**defaults)
