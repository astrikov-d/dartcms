from django import forms
from django.conf import settings
from django.db.models import TextField
from versatileimagefield.datastructures import sizedimage


class RteField(TextField):
    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length, 'widget': forms.Textarea(attrs={'rows': 20, 'class': 'rte'})}
        defaults.update(kwargs)
        return super(RteField, self).formfield(**defaults)


def monkeypatch_versatile_image_field():
    """
    To bypass
    https://github.com/respondcreate/django-versatileimagefield/issues/59
    we monkey patch versatile image field to silent error when
    a specific setting is toggled
    """

    def dec(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except FileNotFoundError:
                if settings.ALLOW_MISSING_MEDIA:
                    return
                raise

        return wrapper

    kls = sizedimage.SizedImage
    kls.create_resized_image = dec(kls.create_resized_image)
