# coding: utf-8
from dartcms.utils.loading import is_model_registered

from .abstract_models import *

__all__ = [
    'FeedType',
    'Feed'
]

if not is_model_registered('feeds', 'FeedItem'):
    class FeedItem(AbstractFeedItem):
        pass

    __all__.append('FeedItem')
