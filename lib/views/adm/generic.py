# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import json
import re
import datetime

from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.paginator import InvalidPage
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect, Http404
from django.utils.translation import ugettext as _

from lib.views.generic import AjaxRequestView


class ModulePermissionsMixin(object):
    """
    Mixin for checking user access permissions for specified CMS module.
    """

    # Check that current user have access to requested module.
    def check_module_perms(self):
        active_module_slug = self.request.path.strip("/").split("/")[0]
        user_modules = [m.slug for m in self.request.user.cmsmodule_set.all()]
        if active_module_slug not in user_modules:
            raise Http404
        return True

    def dispatch(self, request, *args, **kwargs):
        self.check_module_perms()
        response = super(ModulePermissionsMixin, self).dispatch(request, *args, **kwargs)
        return response


class AdminMixin(ModulePermissionsMixin, object):
    """
    Admin mixin. It's common for all admin view. Gets current url sheme, app name etc.
    """

    # True if user can delete records via this app
    allow_delete = True

    # True if user can insert records via this app
    allow_insert = True

    # True if user can update records via this app
    allow_update = True

    # Parent model for children element, used in insert view to create foreign key relation.
    parent_model = None
    parent_model_fk = None

    # URL argument name to get the parent object in children.
    parent_kwarg_name = u''

    # Page header. If page_header == '', model's verbose name used.
    page_header = u''

    # Columns for grid. Model attrib name, Column name, attribute type, width
    grid_columns = (
        ('name', u'Название', "string", "70%"),
        ('date_created', u'Дата создания', "datetime", "30%"),
    )

    # Additional buttons for children records
    object_actions = ()

    # Search fields
    search_by = ()

    # Form class for insert and update views.
    form_class = None

    # Inline elements of the forms
    inlines = []

    # Index app url
    index_url = ""

    def get_context_data(self, *args, **kwargs):
        context = super(AdminMixin, self).get_context_data(*args, **kwargs)

        if 'back_url' in self.request.GET:
            self.index_url = self.request.GET.get('back_url')
        else:
            self.index_url = re.sub(r'(insert/|update/\d+/|page/\d+/|delete/(\d+)/|change-password/(\d+)/)', "",
                                    self.request.path)

        if self.parent_kwarg_name:
            reg = r'(%s/(\d+)/(page/\d+/)?)$' % self.kwargs['children_url']
            print reg
            parent_url = re.sub(reg, "", self.request.path)
        else:
            parent_url = ""
        print parent_url

        context.update({
            'page_header': self.page_header if self.page_header else self.model._meta.verbose_name_plural,
            'parent_kwarg_name': self.parent_kwarg_name,
            'index_url': self.index_url,
            'parent_url': parent_url
        })
        return context

    def get_success_url(self):
        if 'back_url' in self.request.GET:
            self.index_url = self.request.GET.get('back_url')
        else:
            self.index_url = re.sub(r'(insert/|update/\d+/|delete/(\d+)/)', "", self.request.path)
        return self.index_url


class GridView(AdminMixin, ListView):
    template_name = "adm/base/generic/grid.html"
    paginate_by = 15
    allow_empty = True

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
                elif len(field) > 2 and field[2] == 'boolean':
                    filter = lookup
                    term = self.request.GET.get(lookup, False)
                    if term:
                        queryset = queryset.filter(**{
                            filter: True if term else False
                        })
                else:
                    filter = "%s__icontains" % lookup
                    term = self.request.GET.get(lookup, '')
                    queryset = queryset.filter(**{
                        filter: term
                    })

        return queryset

    def paginate_queryset(self, queryset, page_size):
        """
        Paginate the queryset, if needed.
        """
        paginator = self.get_paginator(
            queryset, page_size, orphans=self.get_paginate_orphans(),
            allow_empty_first_page=self.get_allow_empty())
        page_kwarg = self.page_kwarg
        page = self.kwargs.get(page_kwarg) or self.request.GET.get(page_kwarg) or 1
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


from extra_views import CreateWithInlinesView, UpdateWithInlinesView


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