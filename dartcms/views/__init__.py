# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from .mixins import AdminMixin


class GridView(AdminMixin, ListView):
    template_name = 'dartcms/views/grid.html'
    paginate_by = None
    allow_empty = True
    grid_columns = (
        ('name', _('Title'), 'string', '70%'),
        ('date_created', _('Date created'), 'datetime', '30%'),
    )
    grid_actions = ()

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
        context['grid_actions'] = self.grid_actions
        return context


class InsertObjectView(AdminMixin, CreateView):
    template_name = 'dartcms/views/insert.html'

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


class InsertObjectWithInlinesView(AdminMixin, CreateWithInlinesView):
    template_name = 'dartcms/views/insert.html'
    extra = 0

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


class UpdateObjectView(AdminMixin, UpdateView):
    template_name = 'dartcms/views/update.html'


class UpdateObjectWithInlinesView(AdminMixin, UpdateWithInlinesView):
    template_name = 'dartcms/views/update.html'
    extra = 0


class DeleteObjectView(AdminMixin, DeleteView):
    template_name = 'dartcms/views/delete.html'
