# coding: utf-8
import sys

import six
from django.core.serializers.json import Serializer
from django.db import models
from django.utils.encoding import force_text, is_protected_type

if sys.version_info.major == 3:
    unicode = str


class DartCMSSerializer(Serializer):
    """
    Jquery EasyUI format's compatible serializer for django db objects.
    """

    def serialize(self, queryset, **options):
        self.options = options
        self.stream = options.pop('stream', six.StringIO())
        self.selected_fields = options.pop('fields', None)
        self.selected_props = options.pop('props', [])
        self.use_natural_keys = options.pop('use_natural_keys', False)
        self.use_natural_foreign_keys = options.pop('use_natural_foreign_keys', False)
        self.use_natural_primary_keys = options.pop('use_natural_primary_keys', False)

        self.start_serialization()
        self.first = True
        for obj in queryset:
            self.start_object(obj)
            concrete_model = obj._meta.concrete_model
            for field in concrete_model._meta.local_fields:
                if field.serialize:
                    if field.remote_field is None:
                        if self.selected_fields is None or field.attname in self.selected_fields:
                            self.handle_field(obj, field)
                    else:
                        if self.selected_fields is None or field.attname[:-3] in self.selected_fields:
                            self.handle_fk_field(obj, field)
            for field in concrete_model._meta.many_to_many:
                if field.serialize:
                    if self.selected_fields is None or field.attname in self.selected_fields:
                        self.handle_m2m_field(obj, field)
            if self.selected_props:
                for field in self.selected_props:
                    self.handle_prop(obj, field)
            self.end_object(obj)
            if self.first:
                self.first = False
        self.end_serialization()
        return self.getvalue()

    def handle_prop(self, obj, field):
        self._current[field] = getattr(obj, field)
        if callable(self._current[field]):
            self._current[field] = self._current[field]()

    def get_dump_object(self, obj):
        data = self._current
        if not self.use_natural_primary_keys or not hasattr(obj, 'natural_key'):
            data['pk'] = force_text(obj._get_pk_val(), strings_only=True)
        return data

    def handle_field(self, obj, field):
        if isinstance(field, (models.ImageField, models.FileField)):
            value = field.value_from_object(obj)
            if value:
                self._current[field.name] = value.url
            else:
                self._current[field.name] = None
        else:
            value = field.value_from_object(obj)
            if is_protected_type(value):
                self._current[field.name] = value
            else:
                self._current[field.name] = field.value_to_string(obj)

    def handle_fk_field(self, obj, field):
        if self.use_natural_foreign_keys and hasattr(field.remote_field.model, 'natural_key'):
            related = getattr(obj, field.name)
            if related:
                value = related.natural_key()
            else:
                value = None
        else:
            value = unicode(getattr(obj, field.name))
        self._current[field.name] = value
