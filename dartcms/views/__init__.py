# -*- coding: utf-8 -*-
import json
from datetime import datetime

from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from dartcms.utils.db import get_model_field_type, get_model_field_label, get_model_field
from dartcms.utils.forms import DynamicFieldsForm
from dartcms.utils.serialization import DartCMSSerializer
from dartcms.utils.translation import get_date_format
from .mixins import AdminMixin, JSONResponseMixin


class GridView(AdminMixin, JSONResponseMixin, ListView):
    template_name = 'dartcms/views/grid.html'
    paginate_by = None
    allow_empty = True
    grid_columns = [
        {'field': 'name', 'width': '70%'},
        {'field': 'date_created', 'width': '30%'},
    ]
    search = None
    search_form = None
    base_grid_actions = ['insert', 'update', 'delete']
    additional_grid_actions = []
    model_properties = []

    def get_search_form_kwargs(self):
        if 'search' in self.request.GET:
            return {'initial': self.request.GET}
        return {}

    def get_search_form(self):
        if self.search:
            form_kwargs = self.get_search_form_kwargs()

            class SearchForm(DynamicFieldsForm):
                pass

            fields = []
            for item in self.search:
                field_type = get_model_field_type(self.model, item)
                kwargs = {
                    'label': get_model_field_label(self.model, item),
                    'required': False
                }

                if field_type == 'FOREIGN_KEY':
                    kwargs['queryset'] = get_model_field(self.model, item).related_model.objects.all()

                fields.append({'field': item, 'type': field_type, 'kwargs': kwargs})

            form_kwargs['extra'] = fields
            return SearchForm(**form_kwargs)

    def filter_queryset(self, queryset):
        for field in self.search:
            field_type = get_model_field_type(self.model, field)
            if field_type in ('DATETIME', 'DATE', 'TIME'):
                date_from = self.request.GET.get('%s_from' % field, '')
                date_to = self.request.GET.get('%s_to' % field, '')
                if date_from and date_to:
                    queryset = queryset.filter(**{
                        '%s__gte' % field: datetime.strptime(date_from, '%s %%H:%%M:%%S' % get_date_format()),
                        '%s__lte' % field: datetime.strptime(date_to, '%s %%H:%%M:%%S' % get_date_format()),
                    })
            elif field_type == 'BOOLEAN':
                term = self.request.GET.get(field, False)
                if term:
                    queryset = queryset.filter(**{
                        field: True if term else False
                    })
            elif field_type == 'FOREIGN_KEY':
                term = self.request.GET.get(field, '')
                if term:
                    queryset = queryset.filter(**{
                        '%s_id' % field: term
                    })
            else:
                term = self.request.GET.get(field, '')
                if term:
                    queryset = queryset.filter(**{
                        '%s__icontains' % field: term
                    })

        return queryset

    def get_queryset(self):
        page = self.request.GET.get('page')
        rows = self.request.GET.get('rows', self.paginate_by)

        if self.parent_kwarg_name:
            kwarg = self.kwargs[self.parent_kwarg_name]
            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = '%s_id' % self.parent_model.__name__.lower()

            queryset = self.model.objects.filter(**{
                '%s__exact' % fk: kwarg
            })
        else:
            queryset = super(GridView, self).get_queryset()

        if self.search and 'search' in self.request.GET:
            queryset = self.filter_queryset(queryset)

        if page and rows:
            offset = (int(page) - 1) * int(rows)
            limit = int(rows)
            queryset = queryset[offset:offset + limit]

        return queryset

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context.update({
            'grid_columns': self.grid_columns,
            'grid_actions': self.base_grid_actions,
            'additional_grid_actions': self.additional_grid_actions,
            'search_form': self.get_search_form(),
            'date_format': get_date_format()
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return self.render_to_json_response(context, **response_kwargs)
        return super(GridView, self).render_to_response(context, **response_kwargs)

    def get_data(self, context):
        return {
            'rows': json.loads(DartCMSSerializer().serialize(
                queryset=self.get_queryset(),
                props=self.model_properties
            ))  # TODO: refactor.
        }


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
