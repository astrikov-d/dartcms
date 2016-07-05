# coding: utf-8
import re

from django.core.urlresolvers import reverse
from django.http import Http404, JsonResponse


class ModulePermissionsMixin(object):
    def check_module_perms(self):
        root = reverse('dartcms:dashboard:index')
        active_module_slug = self.request.path.replace(root, '').strip('/').split('/')[0]
        user_modules = self.request.user.module_set.all().values_list('slug', flat=True)
        return active_module_slug in user_modules

    def dispatch(self, request, *args, **kwargs):
        if not self.check_module_perms():
            raise Http404

        response = super(ModulePermissionsMixin, self).dispatch(request, *args, **kwargs)
        return response


class AdminMixin(ModulePermissionsMixin):
    # Parent model for children element, used in insert view to create foreign key relation.
    parent_model = None
    parent_model_fk = None

    # URL argument name to get the parent object in children.
    parent_kwarg_name = ''

    # Page header. If page_header == '', model's verbose name used.
    page_header = ''

    # Index URL
    index_url = ''
    success_url = ''

    def get_context_data(self, *args, **kwargs):
        context = super(AdminMixin, self).get_context_data(*args, **kwargs)

        self.index_url = re.sub(r'(insert/\d+/|insert/|update/\d+/|delete/(\d+)/|change-password/(\d+)/)', '',
                                self.request.path)

        if self.parent_kwarg_name:
            reg = r'(%s/(\d+)/(page/\d+/)?)$' % self.kwargs['children_url']
            parent_url = re.sub(reg, '', self.request.path)
        else:
            parent_url = ''

        context.update({
            'page_header': self.page_header if self.page_header else self.model._meta.verbose_name_plural,
            'parent_kwarg_name': self.parent_kwarg_name,
            'index_url': self.index_url,
            'parent_url': parent_url
        })
        return context

    def get_success_url(self):
        if self.success_url:
            return self.success_url

        self.index_url = re.sub(r'(insert/\d+/|insert/|update/\d+/|delete/(\d+)/)', '', self.request.path)
        return self.index_url


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    http_method_names = ['get', 'post']

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        return context