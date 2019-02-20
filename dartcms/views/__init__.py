# coding: utf-8
import json
from datetime import datetime

from django.db.models import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.utils.translation import ugettext as _

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from dartcms.utils.db import get_model_field_type, get_model_field_label, get_model_field
from dartcms.utils.forms import DynamicFieldsForm
from dartcms.utils.serialization import DartCMSSerializer
from dartcms.utils.translation import get_date_format
from .mixins import AdminMixin, JSONResponseMixin


class JSONView(JSONResponseMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)


class GridView(AdminMixin, JSONResponseMixin, ListView):
    template_name = 'dartcms/views/grid.html'
    paginate_by = None
    allow_empty = True
    grid_columns = [
        {'field': 'name', 'width': '70%', 'label': _('Name')},
        {'field': 'date_created', 'width': '30%', 'label': _('Date created'), 'type': 'DATETIME'},
    ]
    search = None
    search_form = None
    base_grid_actions = ['insert', 'update', 'delete']
    additional_grid_actions = []
    model_properties = []
    parent_str = ''
    single_select = True

    def get_search_form_kwargs(self):
        kwargs = {'auto_id': 'id_for_search_%s'}
        if 'search' in self.request.GET:
            kwargs['initial'] = self.request.GET
        return kwargs

    def get_search_form(self):
        if self.search:
            form_kwargs = self.get_search_form_kwargs()

            class SearchForm(DynamicFieldsForm):
                pass

            fields = []
            for item in self.search:
                label = None

                if isinstance(item, dict):
                    label = item.get('label')
                    if 'field' in item:
                        field = item['field']
                    else:
                        raise KeyError('Search dict item does not have "field" key.')
                else:
                    field = item

                field_type = get_model_field_type(self.model, field)
                kwargs = {
                    'label': label if label else get_model_field_label(self.model, field),
                    'required': False
                }

                if field_type == 'FOREIGN_KEY':
                    kwargs['queryset'] = get_model_field(self.model, field).related_model.objects.all()

                fields.append({'field': field, 'type': field_type, 'kwargs': kwargs})

            form_kwargs['extra'] = fields
            return SearchForm(**form_kwargs)

    def filter_queryset(self, queryset):
        for field in self.search:

            if isinstance(field, dict):
                if 'field' in field:
                    field = field['field']
                else:
                    raise KeyError('Search dict item does not have "field" key.')

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
                        field: True if term == 'ON' else False
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

    def get_paginate_by(self, queryset):
        return self.request.GET.get('rows', self.paginate_by)

    def get_queryset(self):
        if self.parent_kwarg_name:
            kwarg = self.kwargs[self.parent_kwarg_name]

            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = '%s_id' % self.parent_model.__name__.lower()

            self.parent_str = self.model._meta.get_field(fk).related_model.objects.get(pk=kwarg)

            queryset = self.model.objects.filter(**{
                '%s__exact' % fk: kwarg
            })
        else:
            queryset = super(GridView, self).get_queryset()

        if self.search and 'search' in self.request.GET:
            queryset = self.filter_queryset(queryset)

        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order')
        if sort and order:
            sort = sort if order == 'asc' else '-%s' % sort
            queryset = queryset.order_by(sort)

        return queryset

    def get_total_rows_count(self):
        queryset = self.get_queryset()
        return queryset.count()

    def get_grid_actions(self):
        perms = self.user_module_permissions
        grid_actions = []

        for action in ['insert', 'update', 'delete']:
            if getattr(perms, 'can_%s' % action, False) and action in self.base_grid_actions:
                grid_actions.append(action)

        return grid_actions

    def get_additional_grid_actions(self):
        perms = self.user_module_permissions
        if not perms:
            return []

        additional_actions = []

        for additional_action in self.additional_grid_actions:
            required_perms = additional_action.get('required_permissions')
            if required_perms:
                if required_perms == '__all__':
                    if all([perms.can_insert, perms.can_update, perms.can_delete]):
                        additional_actions.append(additional_action)
                else:
                    for perm in required_perms:
                        has_perm = getattr(perms, 'can_%s' % perm, False)
                        if has_perm:
                            additional_actions.append(additional_action)
            else:
                additional_actions.append(additional_action)

        return additional_actions

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)
        context.update({
            'grid_columns': self.grid_columns,
            'grid_actions': self.get_grid_actions(),
            'additional_grid_actions': self.get_additional_grid_actions(),
            'search_form': self.get_search_form(),
            'date_format': get_date_format(),
            'urls_kwargs': self.kwargs,
            'parent_str': self.parent_str,
            'single_select': self.single_select
        })
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            return self.render_to_json_response(context, **response_kwargs)
        return super(GridView, self).render_to_response(context, **response_kwargs)

    def get_data(self, context):
        queryset = self.get_queryset()
        page_size = self.get_paginate_by(queryset)
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
        return {
            'total': self.get_total_rows_count(),
            'rows': json.loads(DartCMSSerializer().serialize(
                queryset=queryset,
                props=self.model_properties
            ))  # TODO: refactor.
        }


class InlineErrorsMixin(object):
    @staticmethod
    def get_inline_errors(inlines):
        errors = {}

        for inline in inlines:
            for form in inline:
                for field_name, field_errors in form.errors.items():
                    field = form[field_name]
                    errors[field.html_name] = field_errors

        return errors


class AjaxInsertObjectMixin(AdminMixin, JSONResponseMixin):
    template_name = 'dartcms/views/insert.html'

    def save_object(self, form, **kwargs):
        self.object = form.save(commit=False)
        if self.parent_kwarg_name:
            setattr(self.object, self.get_foreign_key_name(), self.kwargs[self.parent_kwarg_name])
        self.object.save()
        form.save_m2m()

        inlines = kwargs.pop('inlines', [])
        for formset in inlines:
            formset.save()

        return self.object

    def get_initial(self):
        initial = super(AjaxInsertObjectMixin, self).get_initial()
        if self.parent_model_fk and self.parent_kwarg_name in self.kwargs:
            initial.update({
                self.parent_model_fk: self.kwargs[self.parent_kwarg_name]
            })
        return initial


class InsertObjectView(AjaxInsertObjectMixin, CreateView):
    def form_valid(self, form):
        self.save_object(form)
        return self.render_to_json_response({'result': True, 'action': 'INSERT'})

    def form_invalid(self, form):
        return self.render_to_json_response({'result': False, 'errors': form.errors})


class InsertObjectWithInlinesView(InlineErrorsMixin,
                                  AjaxInsertObjectMixin,
                                  CreateWithInlinesView):

    def forms_valid(self, form, inlines):
        self.save_object(form, inlines=inlines)
        return self.render_to_json_response({'result': True, 'action': 'INSERT'})

    def forms_invalid(self, form, inlines):
        errors = form.errors.copy()
        errors.update(self.get_inline_errors(inlines))
        return self.render_to_json_response({'result': False, 'errors': errors})


class AjaxUpdateObjectMixin(AdminMixin, JSONResponseMixin):
    template_name = 'dartcms/views/update.html'


class UpdateObjectView(AjaxUpdateObjectMixin, UpdateView):
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateObjectView, self).get_context_data(*args, **kwargs)
        if not self.user_module_permissions.can_update:
            context['read_only'] = True
        return context

    def form_valid(self, form):
        form.save()
        return self.render_to_json_response({'result': True, 'action': 'UPDATE'})

    def form_invalid(self, form):
        return self.render_to_json_response({'result': False, 'errors': form.errors})


class UpdateObjectWithInlinesView(InlineErrorsMixin,
                                  AjaxUpdateObjectMixin,
                                  UpdateWithInlinesView):

    def forms_valid(self, form, inlines):
        form.save()
        for formset in inlines:
            formset.save()
        return self.render_to_json_response({'result': True, 'action': 'UPDATE'})

    def forms_invalid(self, form, inlines):
        errors = form.errors.copy()
        errors.update(self.get_inline_errors(inlines))
        return self.render_to_json_response({'result': False, 'errors': errors})


class DeleteObjectView(AdminMixin, JSONResponseMixin, DeleteView):
    template_name = 'dartcms/views/delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
        except ProtectedError:
            return self.render_to_json_response({'result': False, 'error': 'PROTECTED'})
        return self.render_to_json_response({'result': True, 'action': 'DELETE'})


class DeleteMultipleObjectView(AdminMixin, JSONResponseMixin, TemplateView):
    template_name = 'dartcms/views/delete.html'
    kwarg_name = 'pks'

    def get(self, request, *args, **kwargs):
        pks = kwargs.get(self.kwarg_name).split(',')
        context = self.get_context_data(count_records=len(pks))
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        pks = kwargs.get(self.kwarg_name).split(',')
        try:
            self.model.objects.filter(pk__in=pks).delete()
        except ProtectedError:
            return self.render_to_json_response({'result': False, 'error': 'PROTECTED'})
        return self.render_to_json_response({'result': True, 'action': 'DELETE'})
