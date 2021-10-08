from dartcms.utils.loading import get_model
from django.forms import ModelForm


class OrderDatailForm(ModelForm):
    class Meta:
        model = get_model('shop', 'OrderDetail')
        exclude = []
