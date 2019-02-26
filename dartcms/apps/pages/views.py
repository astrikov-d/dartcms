# -*- coding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import urlencode
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView, RedirectView

from mptt.utils import get_cached_trees

from dartcms.utils.loading import get_model
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           JSONView, UpdateObjectView)
from dartcms.views.mixins import JSONResponseMixin, ModulePermissionsMixin

Page = get_model('pages', 'Page')
PageModule = get_model('pages', 'PageModule')


class PageTreeView(GridView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('search'):
            context['search_params_str'] = '?%s' % "&".join('{!s}={!s}'.format(
                k, urlencode(v)) for k, v in self.request.GET.items() if k in ['title', 'url', 'module', 'search'])
            context['parent_str'] = _('Search Results')
        return context


class GetTreeView(GridView, JSONResponseMixin):
    model = Page

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, safe=False, **response_kwargs)

    def get_search_res(self):
        qs = self.model.objects.all()
        if self.request.GET.get('title'):
            qs = qs.filter(title__icontains=self.request.GET.get('title'))
        if self.request.GET.get('module'):
            qs = qs.filter(module_id=self.request.GET.get('module'))
        if self.request.GET.get('url'):
            qs = qs.filter(url__icontains=self.request.GET.get('url'))

        if qs.exists():
            qs = qs.get_ancestors(include_self=True)
            home = get_cached_trees(qs)[0]
            return [home.serializable_object_with_children]
        else:
            return []

    def get_data(self, context):
        if self.request.GET.get('search'):
            return self.get_search_res()

        parent_id = self.request.POST.get('id')
        qs = self.object_list.filter(parent_id=parent_id)
        return [obj.serializable_object for obj in qs]


class PageFormKwargsMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SecurityMixin:
    def has_perm(self):
        if self.request.user.is_superuser:
            return True

        security_type = self.check_object.get_security_type()
        if security_type == 'GROUPS_ONLY':
            return len(
                set(self.request.user.user_groups.all()).intersection(set(self.check_object.user_groups.all()))) > 0
        return True

    def check_object(self):
        raise NotImplemented

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_perm'] = self.has_perm()
        return context


class InsertPageView(SecurityMixin, PageFormKwargsMixin, InsertObjectView):
    @cached_property
    def check_object(self):
        return self.model.objects.get(pk=self.request.GET['parent'])

    def get_initial(self):
        return {'parent': self.check_object}

    def form_valid(self, form):
        obj = self.save_object(form)
        data = {
            'pk': obj.pk,
            'title': obj.title,
            'module': obj.module.name,
            'url': obj.url
        }
        return self.render_to_json_response({'result': True, 'action': 'INSERT', 'data': data})


class UpdatePageView(SecurityMixin, PageFormKwargsMixin, UpdateObjectView):
    @cached_property
    def check_object(self):
        return self.object

    def form_valid(self, form):
        obj = form.save()
        data = {
            'title': obj.title,
            'module': obj.module.name,
            'url': obj.url
        }
        return self.render_to_json_response({'result': True, 'action': 'UPDATE', 'data': data})


class TreeActionView(SecurityMixin, ModulePermissionsMixin, JSONView):
    @cached_property
    def check_object(self):
        return Page.objects.get(pk=self.request.GET.get('source'))

    def get_pages(self):
        target_id = self.request.GET.get('target')
        source_id = self.request.GET.get('source')

        if target_id and source_id:
            target = Page.objects.get(pk=target_id)
            source = Page.objects.get(pk=source_id)

            return target, source

        raise Http404


class AppendPageView(TreeActionView):
    def get_data(self, context):
        if not self.has_perm():
            return {'result': False}

        target, source = self.get_pages()
        source.move_to(target, position='last-child')
        return {'result': True}


class MovePageView(TreeActionView):
    def get_data(self, context):
        if not self.has_perm():
            return {'result': False}

        position = self.request.GET.get('position')
        target, source = self.get_pages()
        if target.parent:
            source.move_to(target, position=position)
            return {'result': True}
        return {'result': False}


class LoadModuleParamsView(ModulePermissionsMixin, JSONView):
    def get_data(self, context):
        try:
            module = PageModule.objects.get(pk=self.request.GET.get('selected_module'))
        except PageModule.DoesNotExist:
            module = None

        if module and module.related_model:
            model_path = module.related_model.split('.')
            app = model_path[0]
            model = model_path[1]
            try:
                RelatedModel = get_model(app, model)
                data = RelatedModel.objects.all()
            except (LookupError, ImportError):
                data = []
        else:
            data = []

        page_pk = self.request.GET.get('pk', 0)

        if page_pk != 0:
            page = Page.objects.get(pk=page_pk)
        else:
            page = None

        params = []

        for item in data:
            if page is not None and page.module == module and str(page.module_params) == str(item.pk):
                params.append({'label': str(item), 'value': item.pk, 'selected': True})
            else:
                params.append({'label': str(item), 'value': item.pk})

        params = sorted(params, key=lambda k: k['label'])

        return {
            'result': True,
            'data': params
        }


class DeletePageView(SecurityMixin, DeleteObjectView):
    @cached_property
    def check_object(self):
        return self.object


class OpenUrlRedirectView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        domain = get_current_site(self.request)
        url = get_object_or_404(Page, pk=self.kwargs.get('pk')).url
        return '//%s%s' % (domain, url)
