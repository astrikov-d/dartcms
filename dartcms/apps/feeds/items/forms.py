# coding: utf-8
from django import forms

from dartcms.utils.loading import get_model


class FeedItemForm(forms.ModelForm):
    class Meta:
        model = get_model('feeds', 'FeedItem')
        exclude = ['feed', 'slug']
