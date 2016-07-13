# coding: utf-8
from django.forms import modelform_factory

from dartcms.views import InsertObjectView, UpdateObjectView, DeleteObjectView
from dartcms.utils.loading import get_model


class FeedbackModelMixin(object):
    def get_form_class(self):
        return {
            'contact': modelform_factory(get_model('feedback', 'ContactMessage')),
            'question': modelform_factory(get_model('feedback', 'QuestionMessage')),
        }


class InsertMessageForm(FeedbackModelMixin, InsertObjectView):
    pass