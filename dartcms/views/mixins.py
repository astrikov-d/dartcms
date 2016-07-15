# coding: utf-8
import re

from django.core.urlresolvers import reverse
from django.http import Http404, JsonResponse


class ModulePermissionsMixin(object):
    def check_module_perms(self):
        if not self.request.user.is_authenticated() or not self.request.user.is_staff:
            return False

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
    parent_model = None
    parent_model_fk = None

    parent_kwarg_name = ''

    page_header = ''

    def get_foreign_key_name(self):
        if self.parent_model_fk or self.parent_model:
            return self.parent_model_fk if self.parent_model_fk else '%s_id' % self.parent_model.__name__.lower()

    def get_context_data(self, *args, **kwargs):
        context = super(AdminMixin, self).get_context_data(*args, **kwargs)

        if self.parent_kwarg_name:
            reg = r'(%s/(\d+)/)$' % self.kwargs['children_url']
            parent_url = re.sub(reg, '', self.request.path)
        else:
            parent_url = ''

        context.update({
            'page_header': self.page_header if self.page_header else self.model._meta.verbose_name_plural,
            'parent_kwarg_name': self.parent_kwarg_name,
            'parent_url': parent_url
        })
        return context


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    http_method_names = ['get', 'post']

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        safe = response_kwargs.pop('safe', None) or False
        return JsonResponse(self.get_data(context), safe=safe, **response_kwargs)

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        return context
