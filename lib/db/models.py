# -*- coding: utf-8 -*-
import copy
import json
from django.utils.text import capfirst
from lib.forms import MultiFileField as MultiFileUploadField, ClearableMultiFileInput
from django.db.models.fields.files import FileField, FieldFile
from django.core.files.base import File
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _


class MultiFileDescriptor(object):
    """
    The descriptor for the file attribute on the model instance. Returns a
    FieldFile when accessed so you can do stuff like::

        >>> instance.file.size

    Assigns a file object on assignment so you can do::

        >>> instance.file = File(...)

    """
    def __init__(self, field):
        self.field = field

    def __get__(self, instance=None, owner=None):
        if instance is None:
            raise AttributeError(
                "The '%s' attribute can only be accessed from %s instances."
                % (self.field.name, owner.__name__))

        # This is slightly complicated, so worth an explanation.
        # instance.file`needs to ultimately return some instance of `File`,
        # probably a subclass. Additionally, this returned object needs to have
        # the FieldFile API so that users can easily do things like
        # instance.file.path and have that delegated to the file storage engine.
        # Easy enough if we're strict about assignment in __set__, but if you
        # peek below you can see that we're not. So depending on the current
        # value of the field we have to dynamically construct some sort of
        # "thing" to return.

        # The instance dict contains whatever was originally assigned
        # in __set__.
        files = instance.__dict__[self.field.name]
        try:
            files = json.loads(files)
        except:
            pass

        files_instance = []
        # If this value is a string (instance.file = "path/to/file") or None
        # then we simply wrap it with the appropriate attribute class according
        # to the file field. [This is FieldFile for FileFields and
        # ImageFieldFile for ImageFields; it's also conceivable that user
        # subclasses might also want to subclass the attribute class]. This
        # object understands how to convert a path to a file, and also how to
        # handle None.
        if files not in EMPTY_VALUES:
            for file in files:
                if isinstance(file, basestring):
                    attr = self.field.attr_class(instance, self.field, file)
                    files_instance.append(attr)

            # Other types of files may be assigned as well, but they need to have
            # the FieldFile interface added to the. Thus, we wrap any other type of
            # File inside a FieldFile (well, the field's attr_class, which is
            # usually FieldFile).
                elif isinstance(file, File) and not isinstance(file, FieldFile):
                    file_copy = self.field.attr_class(instance, self.field, file.name)
                    file_copy.file = file
                    file_copy._committed = False
                    files_instance.append(file_copy)

                # Finally, because of the (some would say boneheaded) way pickle works,
                # the underlying FieldFile might not actually itself have an associated
                # file. So we need to reset the details of the FieldFile in those cases.
                elif isinstance(file, FieldFile) and not hasattr(file, 'field'):
                    file.instance = instance
                    file.field = self.field
                    file.storage = self.field.storage
                else:
                    files_instance.append(file)
        # That was fun, wasn't it?
        return files_instance

    def __set__(self, instance, value):
        instance.__dict__[self.field.name] = value


class MultiFileField(FileField):
    # The class to wrap instance attributes in. Accessing the file object off
    # the instance will always return an instance of attr_class.
    attr_class = FieldFile

    # The descriptor to use for accessing the attribute off of the class.
    descriptor_class = MultiFileDescriptor

    description = _("Files")

    # Internal type for creation database (logtext)
    def get_internal_type(self):
        return "TextField"

    def get_prep_value(self, value):
        "Returns field's value prepared for saving into a database."
        # Need to convert File objects provided via a form to unicode for database insertion
        if value in EMPTY_VALUES:
            return None
        unicode_values = []
        for file in value:
            unicode_values.append(unicode(file))
        return json.dumps(unicode_values)

    def pre_save(self, model_instance, add):
        "Returns field's value just before saving."
        clear = model_instance.__dict__.get('_clear')
        file_list = model_instance.__dict__[self.name]
        if file_list:
            for file in file_list:
                if file and not file._committed:
                    # Commit the file to storage prior to saving the model
                    file.save(file.name, file, save=False)
        if clear:
            fs = copy.copy(file_list)
            for file in clear:
                id = int(file.split('-')[1])
                fs[id].delete(save=False)
        file_list = filter(lambda x: x, file_list) if file_list else []
        return file_list

    def save_form_data(self, instance, data):
        # Important: None means "no change", other false value means "clear"
        # This subtle distinction (rather than a more explicit marker) is
        # needed because we need to consume values that are also sane for a
        # regular (non Model-) Form to find in its cleaned_data dictionary.
        if data is not None:
            # This value will be converted to unicode and stored in the
            # database, so leaving False as-is is not acceptable.
            if not data:
                data = ''
            # getting upload/delete data
            try:
                clear = data.get('clear')
                files = data.get('upload')
            # Exception means that field wasn't changed
            except AttributeError:
                files = data
                clear = None
            if clear:
                setattr(instance, '_clear', clear)
            if files:
                setattr(instance, self.name, files)

    def formfield(self, **kwargs):
        """
        Returns a django.forms.Field instance for this database Field.
        """
        defaults = {'required': not self.blank,
                    'label': capfirst(self.verbose_name),
                    'help_text': self.help_text,
                   }
        if self.has_default():
            if callable(self.default):
                defaults['initial'] = self.default
                defaults['show_hidden_initial'] = True
            else:
                defaults['initial'] = self.get_default()
        defaults.update(kwargs)
        defaults['widget'] = ClearableMultiFileInput
        return MultiFileUploadField(**defaults)

    def south_field_triple(self):
        "Returns a suitable description of this field for South."
        # We'll just introspect the _actual_ field.
        from south.modelsinspector import introspector
        field_class = "django.db.models.fields.TextField"
        args, kwargs = introspector(self)
        # That's our definition!
        return (field_class, args, kwargs)