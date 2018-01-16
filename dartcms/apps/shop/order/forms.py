# coding: utf-8
from dartcms.utils.loading import get_model
from form_utils.forms import BetterModelForm


class OrderForm(BetterModelForm):
    class Meta:
        model = get_model('shop', 'Order')
        exclude = ['user']
