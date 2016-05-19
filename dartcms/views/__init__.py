# -*- coding: utf-8 -*-
import json
import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import InvalidPage
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import ugettext as _

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from .mixins import AdminMixin
from ..utils.hashing import md5
from ..utils.pagination import DiggPaginator


class AjaxRequestView(View):
    """
    Simple ajax response view.
    """

    def get_response(self, request, *args, **kwargs):
        """
        You should redefine this method.
        """
        return {}

    def process_request(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        response = self.get_response(request, *args, **kwargs)
        return self.send_response(response)

    def get(self, request, *args, **kwargs):
        return self.process_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.process_request(request, *args, **kwargs)

    def send_response(self, response):
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='text/html')


class GridView(AdminMixin, ListView):
    template_name = "adm/base/generic/grid.html"
    paginate_by = 15
    paginator_class = DiggPaginator
    allow_empty = True
    __search = False

    def get_page(self):
        url = self.request.path
        url_id = 'pg_%s' % md5()
        page = self.request.GET.get(self.page_kwarg)
        if page:
            self.request.session[url_id] = page
        else:
            referer = self.request.META.get('HTTP_REFERER')
            if referer and referer.find(url) >= 0:
                page = self.request.session.get(url_id, 1)
            else:
                self.request.session[url_id] = 1
                page = 1
        return page

    def get_queryset(self):
        if self.parent_kwarg_name:
            kwarg = self.kwargs[self.parent_kwarg_name]
            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = "%s_id" % self.parent_model.__name__.lower()
            filter = "%s__exact" % fk

            queryset = self.model.objects.filter(**{
                filter: kwarg
            })
        else:
            queryset = super(GridView, self).get_queryset()

        # Search database
        if self.search_by:
            for field in self.search_by:
                lookup = field[0]
                if len(field) > 2 and field[2] in ['datetime', 'date', 'time']:
                    date_from = self.request.GET.get("%s_from" % lookup, '')
                    date_to = self.request.GET.get("%s_to" % lookup, '')
                    filter_from = "%s__gte" % lookup
                    filter_to = "%s__lte" % lookup
                    if date_from and date_to:
                        queryset = queryset.filter(**{
                            filter_from: datetime.datetime.strptime(date_from, "%d.%m.%Y %H:%M:%S"),
                            filter_to: datetime.datetime.strptime(date_to, "%d.%m.%Y %H:%M:%S"),
                        })
                        self.__search = True
                elif len(field) > 2 and field[2] == 'boolean':
                    filter = lookup
                    term = self.request.GET.get(lookup, False)
                    if term:
                        queryset = queryset.filter(**{
                            filter: True if term else False
                        })
                        self.__search = True
                elif field[2] in ('choices', 'foreign_key'):
                    filter = lookup
                    term = self.request.GET.get(lookup, '')
                    if term:
                        queryset = queryset.filter(**{
                            filter: term
                        })
                else:
                    filter = "%s__icontains" % lookup
                    term = self.request.GET.get(lookup, '')
                    queryset = queryset.filter(**{
                        filter: term
                    })
                    if term:
                        self.__search = True

        if self.initial_filter and not self.__search:
            queryset = queryset.filter(**self.initial_filter)
        return queryset

    def paginate_queryset(self, queryset, page_size):
        """
        Paginate the queryset, if needed.
        """

        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())

        page = self.get_page()
        try:
            page_number = int(page)
        except ValueError:
            if page == 'last':
                page_number = paginator.num_pages
            else:
                raise Http404(_("Page is not 'last', nor can it be converted to an int."))
        try:
            page = paginator.page(page_number)
        except InvalidPage as e:
            page = paginator.page(paginator.num_pages)
        return (paginator, page, page.object_list, page.has_other_pages())

    def get_context_data(self, **kwargs):
        context = super(GridView, self).get_context_data(**kwargs)

        if self.search_by:
            # Populate context by search fields
            search_values = []
            for search_field in self.search_by:
                if len(search_field) > 2 and search_field[2] in ['datetime', 'date', 'time']:
                    date_list = [self.request.GET.get("%s_from" % search_field[0], ''),
                                 self.request.GET.get("%s_to" % search_field[0], '')]
                    search_values.append(date_list)
                else:
                    search_values.append(self.request.GET.get(search_field[0], ''))
            context.update({
                'search_values': search_values
            })

        context.update({
            'grid_columns': self.grid_columns,
            'object_actions': self.object_actions,
            'multiple_select': self.multiple_select,
            'allow_insert': self.allow_insert,
            'allow_delete': self.allow_delete,
            'allow_update': self.allow_update,
            'search_by': self.search_by
        })
        return context


class DataGridView(GridView):
    template_name = "adm/base/generic/datagrid.html"
    paginate_by = None

    def get(self, request, *args, **kwargs):
        if request.is_ajax() and request.method == "GET":
            self.object_list = self.get_queryset()
            allow_empty = self.get_allow_empty()

            if not allow_empty:
                if self.get_paginate_by(self.object_list is not None and hasattr(self.object_list, 'exists')):
                    is_empty = not self.object_list.exists()
                else:
                    is_empty = len(self.object_list) == 0
                if is_empty:
                    response = []
                    return self.send_response(response)
            response = list(self.object_list.values())
            return self.send_response(response)

        return super(GridView, self).get(request, *args, **kwargs)

    def send_response(self, response):
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='text/html')


class SortableTreeGridView(GridView):
    template_name = "adm/base/generic/sortable_tree_grid.html"
    paginate_by = None


class SortableTreeGridMoveView(AjaxRequestView):
    model = None

    def get_response(self, request, *args, **kwargs):
        try:
            elem = self.model.objects.get(pk=kwargs['pk'])
            parent = self.model.objects.get(pk=request.POST.get('parent', 1))
            elem.sort = request.POST.get('sort', 1)
            elem.parent = parent
            elem.save()
            return {
                'result': 'success'
            }
        except self.model.DoesNotExist:
            raise Http404


class InsertObjectView(AdminMixin, CreateView):
    template_name = "adm/base/generic/insert.html"

    def form_valid(self, form):
        if self.parent_kwarg_name:
            obj = form.save(commit=False)

            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = "%s_id" % self.parent_model.__name__.lower()

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


class InsertObjectWithInlinesView(AdminMixin, CreateWithInlinesView):
    template_name = "adm/base/generic/insert.html"
    extra = 0

    def forms_valid(self, form, inlines):
        if self.parent_kwarg_name:
            obj = form.save(commit=False)

            if self.parent_model_fk is not None:
                fk = self.parent_model_fk
            else:
                fk = "%s_id" % self.parent_model.__name__.lower()

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


class UpdateObjectView(AdminMixin, UpdateView):
    template_name = "adm/base/generic/update.html"


class UpdateObjectWithInlinesView(AdminMixin, UpdateWithInlinesView):
    template_name = "adm/base/generic/update.html"
    extra = 0


class DeleteObjectView(AdminMixin, DeleteView):
    template_name = "adm/base/generic/delete.html"
