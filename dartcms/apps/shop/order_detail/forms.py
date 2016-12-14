# coding: utf-8
from form_utils.forms import BetterModelForm

from dartcms.utils.loading import get_model


class OrderDatailForm(BetterModelForm):
    class Meta:
        model = get_model('shop', 'OrderDetail')
        exclude = []
