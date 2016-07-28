# coding: utf-8
from django.forms.models import modelform_factory
from django.http import Http404

from dartcms import get_model
from dartcms.views import GridView, InsertObjectView, UpdateObjectView, DeleteObjectView


class DictsFormMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, exclude=[])

    def get_model(self):
        app_label = self.kwargs['app_label']
        model_name = self.kwargs['model_name'].replace('_', ' ').title().replace(' ', '')
        try:
            return get_model(app_label, model_name)
        except:
            raise Http404('Model %s not found' % model_name)

    def dispatch(self, request, *args, **kwargs):
        self.model = self.get_model()
        return super(DictsFormMixin, self).dispatch(request, *args, **kwargs)


class GridDictsView(DictsFormMixin, GridView):
    search = ['name']


class InsertDictsView(DictsFormMixin, InsertObjectView):
    pass


class UpdateDictsView(DictsFormMixin, UpdateObjectView):
    pass


class DeleteDictsView(DictsFormMixin, DeleteObjectView):
    pass
