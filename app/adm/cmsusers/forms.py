__author__ = 'astrikovd'

from django import forms
from django.contrib.auth.models import User

from app.models import CMSModule


class CMSUserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'date_joined', 'user_permissions', 'groups')

    modules = forms.ModelMultipleChoiceField(queryset=CMSModule.objects.all())

    def save(self, commit=True):
        obj = super(CMSUserForm, self).save()
        data = self.cleaned_data

        if obj.id:
            obj.cmsmodule_set.clear()

        for module in data.get('modules', []):
            obj.cmsmodule_set.add(module)

        return obj