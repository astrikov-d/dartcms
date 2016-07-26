# coding: utf-8
from django.forms import modelform_factory

from dartcms.utils.loading import get_model
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           UpdateObjectView)

MESSAGES_MODELS_MAPPING = {
    'contact': get_model('feedback', 'ContactMessage'),
    'question': get_model('feedback', 'QuestionMessage'),
}


class DynamicModelMixin(object):
    def setup_model(self):
        form_type = get_model('feedback', 'FormType').objects.get(pk=self.kwargs['form_type'])
        self.model = MESSAGES_MODELS_MAPPING.get(form_type.slug)

    def get_queryset(self):
        self.setup_model()
        return super(DynamicModelMixin, self).get_queryset()


class FeedbackModelMixin(DynamicModelMixin):
    def get_form_class(self):
        self.setup_model()
        return modelform_factory(self.model, exclude=['type'])


class MessagesGridView(DynamicModelMixin, GridView):
    pass


class UpdateMessageFormView(FeedbackModelMixin, UpdateObjectView):
    pass


class DeleteMessageFormView(FeedbackModelMixin, DeleteObjectView):
    pass


class InsertMessageFormView(FeedbackModelMixin, InsertObjectView):
    pass
