# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

# -*- coding: utf-8 -*-
from django.forms.fields import FileField
from django.forms.widgets import CheckboxInput, FILE_INPUT_CONTRADICTION
from django.forms.widgets import Input
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.html import escape, conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDict, MergeDict
from django.core.exceptions import ValidationError
# Provide this import for backwards compatibility.
from django.core.validators import EMPTY_VALUES
import re

FILE_INPUT_EMPTY_VALUE = object()


class MultiFileInput(Input):
    input_type = 'file'
    needs_multipart_form = True

    def render(self, name, value, attrs=None):
        if attrs is None:
            attrs = {}

        name += '[]'
        attrs['multiple'] = 'multiple'

        return super(MultiFileInput, self).render(name, None, attrs=attrs)

    def value_from_datadict(self, data, files, name):
        """
        File widgets take data from FILES, not POST
        we need to add [] because it's from w3c recommendation
        """
        name += '[]'
        if isinstance(files, (MultiValueDict, MergeDict)):
            return files.getlist(name)
        return files.get(name, None)

    def _has_changed(self, initial, data):
        print data
        if data is None:
            return False
        return True


class ClearableMultiFileInput(MultiFileInput):
    initial_text = ugettext('Currently')
    input_text = ugettext('Change')
    clear_checkbox_label = ugettext('Delete')

    template_with_initial = '<p class="file-upload">%(initial_text)s: %(initial)s %(clear_template)s</p>'

    template_with_clear = '<span class="clearable-file-input">%(clear)s <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label></span>'

    def clear_checkbox_name(self, i, name):
        """
        Given the name of the file input, return the name of the clear checkbox
        input.
        """
        return name + '-' + str(i) + '-clear'

    def clear_checkbox_id(self, name):
        """
        Given the name of the clear checkbox input, return the HTML id for it.
        """
        return name + '_id'

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        input_template = '%(input)s'
        init_template = ''
        substitutions['input'] = super(ClearableMultiFileInput, self).render(name, value, attrs)
        if value is not None:
            # for validation empty value
            for i, file in enumerate(value):
                if file and hasattr(file, "url"):
                    template = self.template_with_initial
                    substitutions['initial'] = ('<a href="%s">%s</a>&nbsp;'
                                                % (escape(file.url),
                                                   escape(force_unicode(file))))
                    if self.is_required or len(value) > 1:
                        checkbox_name = self.clear_checkbox_name(i, name)
                        checkbox_id = self.clear_checkbox_id(checkbox_name)
                        substitutions['clear_checkbox_name'] = conditional_escape(checkbox_name)
                        substitutions['clear_checkbox_id'] = conditional_escape(checkbox_id)
                        substitutions['clear'] = CheckboxInput().render(checkbox_name, False, attrs={'id': checkbox_id})
                        substitutions['clear_template'] = self.template_with_clear % substitutions
                    init_template += (template % substitutions)
            init_template += '<input type="hidden" value="%s" name="total_files">' % len(value)
        return mark_safe(init_template + (input_template % substitutions))

    def value_from_datadict(self, data, files, name):
        upload = super(ClearableMultiFileInput, self).value_from_datadict(data, files, name)
        clear = self._get_clear_list(data, files, name)
        total_files = data.get('total_files', '1')
        if total_files.isdigit():
            total_files = int(total_files)
        if clear not in EMPTY_VALUES:
            if upload:
                # If the user contradicts themselves (uploads a new file AND
                # checks the "clear" checkbox), we return a unique marker
                # object that FileField will turn into a ValidationError.
                return FILE_INPUT_CONTRADICTION
                # If the user delete all files and field is not allow empty values,
                # we return a unique marker
                # object that FileField will turn into a ValidationError.
            if self.is_required and total_files <= len(clear):
                return FILE_INPUT_EMPTY_VALUE
            return {'clear': clear}
        if upload not in EMPTY_VALUES:
            return {'upload': upload}
        return None


    def _get_clear_list(self, data, files, name):
        pattern = re.compile('%s-\d+-clear' % name)
        clear = []
        for key, value in data.iteritems():
            if pattern.match(key) and value == 'on':
                clear.append(key)
        return clear


class MultiFileField(FileField):
    widget = ClearableMultiFileInput
    default_error_messages = {
        'empty_multiply': _("The submitted field is empty! If you want to change all your files, please, select files!")
    }

    def to_python(self, data):
        if data in EMPTY_VALUES:
            return None
        if data is FILE_INPUT_EMPTY_VALUE:
            raise ValidationError(self.error_messages['empty_multiply'])

        # UploadedFile objects should have name and size attributes.
        for d in data.get('upload', []):
            try:
                file_name = d.name
                file_size = d.size
            except AttributeError:
                raise ValidationError(self.error_messages['invalid'])

            if self.max_length is not None and len(file_name) > self.max_length:
                error_values = {'max': self.max_length, 'length': len(file_name)}
                raise ValidationError(self.error_messages['max_length'] % error_values)
            if not file_name:
                raise ValidationError(self.error_messages['invalid'])
            if not self.allow_empty_file and not file_size:
                raise ValidationError(self.error_messages['empty'])
        return data


    def bound_data(self, data, initial):
        if data in (None, FILE_INPUT_CONTRADICTION, FILE_INPUT_EMPTY_VALUE):
            return initial
        return data


class AdminMultiFileInputWidget(ClearableMultiFileInput):
    template_with_initial = (u'<p class="file-upload">%s</p>'
                             % ClearableMultiFileInput.template_with_initial)
    template_with_clear = (u'<span class="clearable-file-input">%s</span>'
                           % ClearableMultiFileInput.template_with_clear)