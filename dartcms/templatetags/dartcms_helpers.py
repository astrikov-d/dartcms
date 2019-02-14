# coding: utf-8
import json
import os
import types

from django import template
from django.forms import (CheckboxInput, CheckboxSelectMultiple,
                          ClearableFileInput, DateInput, DateTimeInput,
                          HiddenInput, RadioSelect, SelectMultiple)
from widget_tweaks.templatetags.widget_tweaks import (append_attr,
                                                      silence_without_field)

from .ifstartswith import do_startswith

try:
    import Image, ImageOps
except ImportError:
    from PIL import Image, ImageOps

register = template.Library()


#######################################################################################
# Startswith template tags.                                                           #
# Usage:                                                                              #
# {% ifstartswith foo 'bar' %}                                                        #
# ...                                                                                 #
# {% endifstartswith %}                                                               #
#######################################################################################


@register.tag
def ifstartswith(parser, token):
    return do_startswith(parser, token, False)


@register.tag
def ifnotstartswith(parser, token):
    return do_startswith(parser, token, True)


#######################################################################################
# Thumbnail filters.                                                                  #
#######################################################################################


@register.filter
def thumbnail(file, size='220x220'):
    x, y = [int(x) for x in size.split('x')]
    if isinstance(file, str):
        file = open(file, 'rw')

    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
        # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename) and os.path.exists(filename):
        image = Image.open(filename)

        if (image.size[0] < x):
            x = image.size[0]
        if (image.size[1] < y):
            y = image.size[1]

        img_ratio = float(image.size[0]) / image.size[1]
        # resize but constrain proportions?
        if x == 0.0:
            x = y * img_ratio
        elif y == 0.0:
            y = x / img_ratio

        thumb_ratio = float(x) / y
        x = int(x);
        y = int(y)

        if (img_ratio > thumb_ratio):
            c_width = x * image.size[1] / y
            c_height = image.size[1]
            originX = image.size[0] / 2 - c_width / 2
            originY = 0
        else:
            c_width = image.size[0]
            c_height = y * image.size[0] / x
            originX = 0
            originY = image.size[1] / 2 - c_height / 2

        cropBox = (originX, originY, originX + c_width, originY + c_height)
        image = image.crop(cropBox)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            try:
                image.save(miniature_filename, image.format, quality=90)
            except:
                return None

    return miniature_url


@register.filter
def thumbnail_with_max_side(file, size='220'):
    filehead, filetail = os.path.split(file.path)
    basename, format = os.path.splitext(filetail)
    miniature = basename + '_' + size + format
    filename = file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    if not os.path.exists(miniature_filename) and os.path.exists(filename):
        image = Image.open(filename)
        x, y = 0, 0

        if (image.size[0] < x) or (image.size[1] < y):
            return filehead + '/' + basename + format

        img_ratio = float(image.size[0]) / image.size[1]
        if img_ratio > 1:
            x = int(size)
        else:
            y = int(size)
        if x == 0.0:
            x = y * img_ratio
        elif y == 0.0:
            y = x / img_ratio

        thumb_ratio = float(x) / y

        x = int(x)
        y = int(y)

        if (img_ratio > thumb_ratio):
            c_width = x * image.size[1] / y
            c_height = image.size[1]
            originX = image.size[0] / 2 - c_width / 2
            originY = 0
            cropBox = (originX, originY, originX + c_width, originY + c_height)
            image = image.crop(cropBox)
        else:
            c_width = image.size[0]
            c_height = y * image.size[0] / x
            originX = 0
            originY = image.size[1] / 2 - c_height / 2
            cropBox = (originX, originY, originX + c_width, originY + c_height)
            image = image.crop(cropBox)

        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url


#######################################################################################
# File-related filters.                                                               #
#######################################################################################


@register.filter
def filename(value):
    return os.path.basename(str(value))


@register.filter
def ext(value):
    name, extension = os.path.splitext(value.name.lower())
    return extension.replace('.', '')


#######################################################################################
# Attribute lookup filters                                                            #
#######################################################################################


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def attribute(obj, attribute_name):
    return getattr(obj, attribute_name, None)


#######################################################################################
# Form helpers.                                                                       #
#######################################################################################


@register.filter
def is_checkbox(field):
    return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter
def is_hidden(field):
    return field.field.widget.__class__.__name__ == HiddenInput().__class__.__name__


@register.filter
def is_file(field):
    return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__


@register.filter
def is_radio(field):
    return field.field.widget.__class__.__name__ == RadioSelect().__class__.__name__


@register.filter
def is_date(field):
    return field.field.widget.__class__.__name__ == DateInput().__class__.__name__


@register.filter
def is_datetime(field):
    return field.field.widget.__class__.__name__ == DateTimeInput().__class__.__name__


@register.filter
def is_multiple_select(field):
    return field.field.widget.__class__.__name__ == SelectMultiple().__class__.__name__


@register.filter
def is_checkbox_multiple_select(field):
    return field.field.widget.__class__.__name__ == CheckboxSelectMultiple().__class__.__name__


@register.filter
def test_widget_class(field):
    return field.field.widget.__class__.__name__


#######################################################################################
# Widget tweaks backport.                                                             #
#######################################################################################


def _process_field_attributes(field, attr, process):
    params = attr.split(':', 1)
    attribute = params[0]
    value = params[1] if len(params) == 2 else ''

    old_as_widget = field.as_widget

    def as_widget(self, widget=None, attrs=None, only_initial=False):
        attrs = attrs or {}
        process(widget or self.field.widget, attrs, attribute, value)
        html = old_as_widget(widget, attrs, only_initial)
        self.as_widget = old_as_widget
        return html

    field.as_widget = types.MethodType(as_widget, field)
    return field


@register.filter('attr')
@silence_without_field
def set_attr(field, attr):
    def process(widget, attrs, attribute, value):
        attrs[attribute] = value

    return _process_field_attributes(field, attr, process)


@register.filter('add_error_attr')
@silence_without_field
def add_error_attr(field, attr):
    if hasattr(field, 'errors') and field.errors:
        return set_attr(field, attr)
    return field


@register.filter('add_class')
@silence_without_field
def add_class(field, css_class):
    return append_attr(field, 'class:' + css_class)


#######################################################################################
# Tinymce settings                                                                    #
#######################################################################################
@register.simple_tag
def get_tinymce_settings():
    from django.conf import settings
    return getattr(settings, 'DARTCMS_TINYMCE_SETTINGS', {})


#######################################################################################
# Useful utils                                                                        #
#######################################################################################
@register.filter('get_type')
def get_type(value):
    mapping = {
        str: 'str',
        dict: 'dict',
        list: 'list',
        tuple: 'tuple',
        bool: 'bool',
        int: 'int'
    }
    return mapping.get(type(value))


@register.filter('json_loads')
def json_loads(value):
    return json.loads(value)


@register.filter('json_dumps')
def json_dumps(value):
    return json.dumps(value)
