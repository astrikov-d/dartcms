# coding: utf-8
import re

from django.http import Http404


class ModulePermissionsMixin(object):
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


class AdminMixin(ModulePermissionsMixin):
    """
    Admin mixin. It's common for all admin view. Gets current url scheme, app name etc.
    """

    initial_filter = {}

    allow_delete = True
    allow_insert = True
    allow_update = True

    # True if user can select multiple rows
    # USAGE:
    #
    # Add this action to your urls.py
    #
    # object_actions = (
    #    (u"Button Name", u'button-url', u'fa-check', 'success', 'multiple-action'),
    # )
    multiple_select = False

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

        self.index_url = re.sub(r'(insert/\d+/|insert/|update/\d+/|page/\d+/|delete/(\d+)/|change-password/(\d+)/)', "",
                                self.request.path)

        if self.parent_kwarg_name:
            reg = r'(%s/(\d+)/(page/\d+/)?)$' % self.kwargs['children_url']
            parent_url = re.sub(reg, "", self.request.path)
        else:
            parent_url = ""

        context.update({
            'page_header': self.page_header if self.page_header else self.model._meta.verbose_name_plural,
            'parent_kwarg_name': self.parent_kwarg_name,
            'index_url': self.index_url,
            'parent_url': parent_url
        })
        return context

    def get_success_url(self):
        self.index_url = re.sub(r'(insert/\d+/|insert/|update/\d+/|delete/(\d+)/)', "", self.request.path)
        return self.index_url
