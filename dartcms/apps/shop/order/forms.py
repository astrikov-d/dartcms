from dartcms.utils.loading import get_model
from django.forms import ModelForm


class OrderForm(ModelForm):
    class Meta:
        model = get_model('shop', 'Order')
        exclude = ['user']
