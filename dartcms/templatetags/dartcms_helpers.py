# coding: utf-8
import os

try:
    import Image, ImageOps
except ImportError:
    from PIL import Image, ImageOps

from django import template
from django.template import Node, NodeList, Variable, VariableDoesNotExist

register = template.Library()


def do_startswith(parser, token, negate):
    try:
        tag_name, string, start_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires two arguments" % token.contents.split()[0]
    end_tag = 'end' + tag_name
    nodelist_true = parser.parse(('else', end_tag))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse((end_tag,))
        parser.delete_first_token()
    else:
        nodelist_false = NodeList()
    return IfStartsWithNode(string, start_string, nodelist_true, nodelist_false, negate)


class IfStartsWithNode(Node):
    def __init__(self, string, start_string, nodelist_true, nodelist_false, negate):
        self.start_string, self.string = Variable(start_string), Variable(string)
        self.nodelist_true, self.nodelist_false = nodelist_true, nodelist_false
        self.negate = negate
        self.negate = negate

    def __repr__(self):
        return "<IfStartsWithNode>"

    def render(self, context):
        try:
            string = self.string.resolve(context)
        except VariableDoesNotExist:
            string = None
        try:
            start_string = self.start_string.resolve(context)
        except VariableDoesNotExist:
            start_string = None

        if (self.negate and not string.startswith(start_string)) or (
                    not self.negate and string.startswith(start_string)):
            return self.nodelist_true.render(context)
        return self.nodelist_false.render(context)


def ifstartswith(parser, token):
    return do_startswith(parser, token, False)


ifstartswith = register.tag(ifstartswith)


def ifnotstartswith(parser, token):
    return do_startswith(parser, token, True)


ifnotstartswith = register.tag(ifnotstartswith)


def thumbnail(file, size='220x220'):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
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
    if not os.path.exists(miniature_filename):
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
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url


def thumbnail_with_max_side(file, size='220'):
    # defining the filename and the miniature filename
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
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        x, y = 0, 0

        if (image.size[0] < x) or (image.size[1] < y):
            return filehead + '/' + basename + format

        img_ratio = float(image.size[0]) / image.size[1]
        if img_ratio > 1:
            x = int(size)
        else:
            y = int(size)
            # resize but constrain proportions?
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


register.filter(thumbnail)
register.filter(thumbnail_with_max_side)


@register.filter
def filename(value):
    return os.path.basename(str(value))


@register.filter
def ext(value):
    name, extension = os.path.splitext(value.name.lower())
    return extension.replace('.', '')


@register.filter
def lookup(d, key):
    return d[key]


@register.filter
def attribute(obj, attribute_name):
    return getattr(obj, attribute_name, None)
