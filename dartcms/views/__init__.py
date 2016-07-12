# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from .mixins import AdminMixin, JSONResponseMixin


class GridView(AdminMixin, ListView):
    template_name = 'dartcms/views/grid.html'
    paginate_by = None
    allow_empty = True
    grid_columns = [
        {'field': 'name', 'width': '70%'},
        {'field': 'date_created', 'width': '30%'},
    ]
    base_grid_actions = ['insert', 'update', 'delete']
    additional_grid_actions = []

    def get_queryset(self):
        if self.parent_kwarg_name:
            kwarg = self.kwargs[self.parent_kwarg_name]
            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = '%s_id' % self.parent_model.__name__.lower()
            query_filter = '%s__exact' % fk

            queryset = self.model.objects.filter(**{
                query_filter: kwarg
            })
        else:
            queryset = super(GridView, self).get_queryset()

        return queryset

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context['grid_columns'] = self.grid_columns
        context['grid_actions'] = self.base_grid_actions
        context['additional_grid_actions'] = self.additional_grid_actions
        return context


class InsertObjectView(AdminMixin, SuccessMessageMixin, CreateView):
    template_name = 'dartcms/views/insert.html'
    success_message = _('Record successfully added')

    def form_valid(self, form):
        if self.parent_kwarg_name:
            obj = form.save(commit=False)

            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = '%s_id' % self.parent_model.__name__.lower()

            setattr(obj, fk, self.kwargs[self.parent_kwarg_name])
            obj.save()
            form.save_m2m()
            self.object = obj
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(InsertObjectView, self).form_valid(form)

    def get_initial(self):
        initial = super(InsertObjectView, self).get_initial()
        if self.parent_model_fk and self.parent_kwarg_name in self.kwargs:
            initial.update({
                self.parent_model_fk: self.kwargs[self.parent_kwarg_name]
            })
        return initial


class InsertObjectWithInlinesView(AdminMixin, SuccessMessageMixin, CreateWithInlinesView):
    template_name = 'dartcms/views/insert.html'
    extra = 0
    success_message = _('Record successfully added')

    def forms_valid(self, form, inlines):
        if self.parent_kwarg_name:
            obj = form.save(commit=False)

            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = '%s_id' % self.parent_model.__name__.lower()

            setattr(obj, fk, self.kwargs[self.parent_kwarg_name])
            obj.save()

            for formset in inlines:
                formset.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(InsertObjectWithInlinesView, self).form_valid(form)

    def get_initial(self):
        initial = super(InsertObjectWithInlinesView, self).get_initial()
        if self.parent_model_fk and self.parent_kwarg_name in self.kwargs:
            initial.update({
                self.parent_model_fk: self.kwargs[self.parent_kwarg_name]
            })
        return initial


class UpdateObjectView(AdminMixin, SuccessMessageMixin, UpdateView):
    template_name = 'dartcms/views/update.html'
    success_message = _('Record successfully updated')


class UpdateObjectWithInlinesView(AdminMixin, SuccessMessageMixin, UpdateWithInlinesView):
    template_name = 'dartcms/views/update.html'
    extra = 0
    success_message = _('Record successfully updated')


class DeleteObjectView(AdminMixin, SuccessMessageMixin, DeleteView):
    template_name = 'dartcms/views/delete.html'
    success_message = _('Record successfully deleted')


class JSONView(JSONResponseMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)