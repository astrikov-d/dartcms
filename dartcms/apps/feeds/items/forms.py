# coding: utf-8
import datetime

from django import forms
from django.utils.translation import ugettext_lazy as _

from dartcms.utils.loading import get_model


class FeedItemForm(forms.ModelForm):
    class Meta:
        model = get_model('feeds', 'FeedItem')
        exclude = ['feed', 'slug']
