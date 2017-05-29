# coding: utf-8
import re

from django.core.urlresolvers import reverse
from django.forms import modelform_factory
from django.http import Http404, JsonResponse
from django.utils.functional import cached_property

from dartcms.apps.modules.functions import get_current_module, get_current_module_perms
from dartcms.utils.loading import get_form_class, get_model


class ModulePermissionsMixin(object):
    def check_module_perms(self):
        if not self.request.user.is_authenticated() or not self.request.user.is_staff:
            return False

        root = reverse('dartcms:dashboard:index')
        active_module_slug = self.request.path.replace(root, '', 1).strip('/').split('/')[0]
        user_modules = self.request.user.module_set.all().values_list('slug', flat=True)
        return active_module_slug in list(user_modules)

    @cached_property
    def user_module_permissions(self):
        return get_current_module_perms(self.request)

    def dispatch(self, request, *args, **kwargs):
        if not self.check_module_perms():
            raise Http404('You don\'t have permissions to this module')

        response = super(ModulePermissionsMixin, self).dispatch(request, *args, **kwargs)
        return response


class AdminMixin(ModulePermissionsMixin):
    config = None

    module = None
    model = None
    form_class = None

    parent_model = None
    parent_model_fk = None

    parent_kwarg_name = ''

    page_header = ''

    def dispatch(self, request, *args, **kwargs):
        self.module = get_current_module(request.path)
        if self.module and self.module.config:
            self.config = self.module.config

            model_label = self.config.get('model', self.model)
            if model_label:
                app_label, model_name = model_label.split('.')
                self.model = get_model(app_label, model_name)

            form_config = self.config.get('form')
            if form_config:
                if 'form_class' in form_config:
                    app_label, form_class_name = form_config['form_class'].split('.')
                    self.form_class = get_form_class(app_label, form_class_name)
                form_fields = form_config.get('fields', '__all__')
                exclude_fields = form_config.get('exclude', [])
            else:
                form_fields = '__all__'
                exclude_fields = []

            if self.form_class is None:
                self.form_class = modelform_factory(self.model, fields=form_fields, exclude=exclude_fields)

            if hasattr(self, 'grid_columns'):
                grid_config = self.config.get('grid')
                if grid_config:
                    self.grid_columns = grid_config.get('grid_columns', self.grid_columns)

                    search_config = grid_config.get('search')
                    if search_config:
                        self.search = search_config

                    self.ordering = grid_config.get('ordering')
                    self.model_properties = grid_config.get('model_properties')

        return super(AdminMixin, self).dispatch(request, *args, **kwargs)

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
