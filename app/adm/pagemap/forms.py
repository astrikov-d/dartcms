# -*- coding: utf-8 -*-

from django.forms import ModelForm, ModelChoiceField, Textarea, Select

from app.models import Page, PageModule, AdvSection


class Form(ModelForm):
    class Meta:
        model = Page
        exclude = ['url', 'date_created', 'date_changed', 'sort']
        widgets = {
            'before_content': Textarea(attrs={'rows': 20, 'class': 'rte'}),
            'after_content': Textarea(attrs={'rows': 20, 'class': 'rte'}),
            'module_params': Select()
        }

    module = ModelChoiceField(PageModule.objects.filter(is_enabled=True), empty_label=None, label="Модуль")
    adv_section = ModelChoiceField(AdvSection.objects.filter(is_enabled=True), empty_label=None, label="Реклама")

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        if self.instance.pk == 1:
            del self.fields['is_enabled']
            del self.fields['is_locked']
            del self.fields['menu_url']
            del self.fields['module']
            del self.fields['parent']
            del self.fields['module_params']
            del self.fields['slug']

        if self.instance.pk and self.instance.pk != 1:
            del self.fields['parent']