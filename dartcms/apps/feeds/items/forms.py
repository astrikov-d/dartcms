# coding: utf-8
import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.loading import get_model


class FeedItemForm(forms.ModelForm):
    class Meta:
        model = get_model('feeds', 'FeedItem')
        exclude = ['feed', 'slug']
        widgets = {
            'short_text': forms.Textarea(attrs={'class': 'rte'}),
            'full_text': forms.Textarea(attrs={'class': 'rte'}),
        }

    date_published = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'datetime'
            }
        ),
        localize=True,
        initial=datetime.datetime.now,
        label=_('Date of publication')
    )