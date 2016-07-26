# coding: utf-8
from dartcms.utils.loading import is_model_registered

from .abstract_models import *

__all__ = [
    'FormType',
]

if not is_model_registered('feedback', 'QuestionMessage'):
    class QuestionMessage(AbstractQuestionMessage):
        pass

    __all__.append('QuestionMessage')

if not is_model_registered('feedback', 'ContactMessage'):
    class ContactMessage(AbstractContactMessage):
        pass

    __all__.append('ContactMessage')
