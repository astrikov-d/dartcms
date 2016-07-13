# coding: utf-8
from django.forms import modelform_factory

from dartcms.views import GridView, UpdateObjectView, DeleteObjectView
from dartcms.utils.loading import get_model


MESSAGES_MODELS_MAPPING = {
    'contact': get_model('feedback', 'ContactMessage'),
    'question': get_model('feedback', 'QuestionMessage'),
}


class DynamicModelMixin(object):
    def setup_model(self):
        form_type = get_model('feedback', 'FormType').objects.get(pk=self.kwargs['form_type'])
        self.model = MESSAGES_MODELS_MAPPING.get(form_type.slug)


class FeedbackModelMixin(DynamicModelMixin):
    def get_form_class(self):
        self.setup_model()
        return modelform_factory(self.model, exclude=['type'])


class MessagesGridView(DynamicModelMixin, GridView):
    def get_queryset(self):
        self.setup_model()
        return super(MessagesGridView, self).get_queryset()


class UpdateMessageFormView(FeedbackModelMixin, UpdateObjectView):
    pass


class DeleteMessageFormView(FeedbackModelMixin, DeleteObjectView):
    pass