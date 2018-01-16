# -*- coding: utf-8 -*-
from dartcms.utils.loading import get_model
from dartcms.views import GridView, InsertObjectView, JSONView
from dartcms.views.mixins import JSONResponseMixin, ModulePermissionsMixin
from django.http import Http404
from django.utils.translation import ugettext as __


class GetTreeView(GridView, JSONResponseMixin):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, safe=False, **response_kwargs)

    def get_data(self, context):
        sections = self.object_list.filter(parent=None)
        tree = [dict(pk='0', parent_id=None, name=__('Root section'), is_visible='', children=[])]
        for section in sections:
            tree[0]['children'].append(section.serializable_object())
        return tree


class InsertSectionView(InsertObjectView):
    def get_initial(self):
        return {'parent': self.model.objects.filter(pk=self.request.GET.get('parent', 0)).first()}


class TreeActionView(ModulePermissionsMixin, JSONView):
    def get_sections(self):
        target_id = self.request.GET.get('target')
        source_id = self.request.GET.get('source')

        if target_id and source_id:
            ProductSection = get_model('shop', 'ProductSection')

            target = ProductSection.objects.get(pk=target_id) if target_id != '0' else None
            source = ProductSection.objects.get(pk=source_id)

            return target, source

        raise Http404


class AppendSectionView(TreeActionView):
    def get_data(self, context):
        target, source = self.get_sections()
        source.move_to(target, position='last-child')
        return {'result': True}


class MoveSectionView(TreeActionView):
    def get_data(self, context):
        position = self.request.GET.get('position')
        target, source = self.get_sections()

        if target:
            source.move_to(target, position=position)
            return {'result': True}
        return {'result': False}
