# coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.loading import get_model
from form_utils.forms import BetterModelForm

PageModule = get_model('pages', 'PageModule')
AdSection = get_model('ads', 'AdSection')


class PageForm(BetterModelForm):
    class Meta:
        model = get_model('pages', 'Page')
        exclude = ['url', 'date_created', 'date_changed', 'sort']
        widgets = {
            'module_params': forms.Select()
        }

        fieldsets = (
            ('main', {'fields': (
                'parent',
                'slug',
                'title',
                'header',
                'menu_name',
                'menu_url',
                'redirect_url',
                'module',
                'module_params',
            ), 'legend': _('Main')}),
            ('content', {'fields': (
                'before_content',
                'after_content',
            ), 'legend': _('Content')}),
            ('ads', {'fields': (
                'ad_section',
            ), 'legend': _('Ads')}),
            ('seo', {'fields': (
                'seo_keywords',
                'seo_description',
            ), 'legend': _('SEO')}),
            ('advanced', {'fields': (
                'is_enabled',
                'is_in_menu',
                'is_locked',
            ), 'legend': _('Advanced')}))

    module = forms.ModelChoiceField(PageModule.objects.filter(is_enabled=True).exclude(slug='homepage'), empty_label=None, label=_('Module'))
    ad_section = forms.ModelChoiceField(AdSection.objects.filter(is_enabled=True), required=False, label=_('Ads'))

    def __init__(self, *args, **kwargs):
        super(PageForm, self).__init__(*args, **kwargs)
        if self.instance.pk and self.instance.module.slug == 'homepage':
            del self.fields['is_enabled']
            del self.fields['redirect_url']
            del self.fields['module']
            del self.fields['parent']
            del self.fields['module_params']
            del self.fields['slug']
        else:
            self.fields['module'].initial = PageModule.objects.get(slug='page')
