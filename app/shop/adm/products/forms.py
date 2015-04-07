__author__ = 'astrikovd'

from extra_views import InlineFormSet

from django import forms

from app.shop.models import ProductPicture


class ProductPictureInline(InlineFormSet):
    exclude = []
    model = ProductPicture
