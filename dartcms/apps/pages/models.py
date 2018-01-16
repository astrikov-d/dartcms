# coding: utf-8

from dartcms.utils.loading import get_model, is_model_registered
from django.db.models.signals import post_save, pre_delete, pre_save

from .abstract_models import *
from .signals import *

__all__ = [
    'PageModule'
]

if is_model_registered('pages', 'Page'):
    page_model = get_model('pages', 'Page')
else:
    class Page(AbstractPage):
        pass

    __all__.append('Page')

    page_model = Page

pre_save.connect(pre_save_handler, sender=page_model)
post_save.connect(post_save_handler, sender=page_model)
pre_delete.connect(pre_delete_handler, sender=page_model)
