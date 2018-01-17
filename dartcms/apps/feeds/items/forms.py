# coding: utf-8
from dartcms.utils.loading import get_model
from django import forms


class FeedItemForm(forms.ModelForm):
    class Meta:
        model = get_model('feeds', 'FeedItem')
        exclude = ['feed', 'slug']
