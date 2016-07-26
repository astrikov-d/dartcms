# -*- coding: utf-8 -*-
from dartcms.utils.loading import is_model_registered

from .abstract_models import *

__all__ = [
    'AdPlace',
    'AdSection'
]

if not is_model_registered('ads', 'Ad'):
    class Ad(AbstractAd):
        pass

    __all__.append('Ad')
