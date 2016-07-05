# -*- coding: utf-8 -*-
from django.http import Http404

from dartcms.utils.loading import get_model

from dartcms.views import GridView, InsertObjectView, JSONView
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


class InsertPageView(InsertObjectView):
    def get_initial(self):
        return {
            'parent': self.model.objects.filter(pk=self.request.GET.get('parent', 0)).first()
        }


class TreeActionView(ModulePermissionsMixin, JSONView):
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
        target, source = self.get_pages()
        source.move_to(target, position='last-child')
        return {'result': True}


class MovePageView(TreeActionView):
    def get_data(self, context):
        position = self.request.GET.get('position')
        target, source = self.get_pages()
        source.move_to(target, position=position)
        return {'result': True}

