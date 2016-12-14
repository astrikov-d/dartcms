# -*- coding: utf-8 -*-
from django.http import Http404
from django.utils.functional import cached_property

from dartcms.utils.loading import get_model
from dartcms.views import (DeleteObjectView, GridView, InsertObjectView,
                           JSONView, UpdateObjectView)
from dartcms.views.mixins import JSONResponseMixin, ModulePermissionsMixin


class GetTreeView(GridView, JSONResponseMixin):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, safe=False, **response_kwargs)

    def get_data(self, context):
        homepage = self.object_list.get(module__slug='homepage')
        tree = [homepage.serializable_object()]
        return tree


class PageFormKwargsMixin(object):
    def get_form_kwargs(self):
        kwargs = super(PageFormKwargsMixin, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class SecurityMixin(object):
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
        context = super(SecurityMixin, self).get_context_data(**kwargs)
        context['has_perm'] = self.has_perm()
        return context


class InsertPageView(SecurityMixin, PageFormKwargsMixin, InsertObjectView):
    @cached_property
    def check_object(self):
        return self.model.objects.get(pk=self.request.GET['parent'])

    def get_initial(self):
        return {'parent': self.check_object}


class UpdatePageView(SecurityMixin, PageFormKwargsMixin, UpdateObjectView):
    @cached_property
    def check_object(self):
        return self.object


class TreeActionView(SecurityMixin, ModulePermissionsMixin, JSONView):
    @cached_property
    def check_object(self):
        Page = get_model('pages', 'Page')
        return Page.objects.get(pk=self.request.GET.get('source'))

    def get_pages(self):
        target_id = self.request.GET.get('target')
        source_id = self.request.GET.get('source')

        if target_id and source_id:
            Page = get_model('pages', 'Page')

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
        PageModule = get_model('pages', 'PageModule')
        Page = get_model('pages', 'Page')

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
