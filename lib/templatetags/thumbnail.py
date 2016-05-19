__author__ = 'Dmitry Astrikov'

import os

try:
    import Image, ImageOps
except ImportError:
    from PIL import Image, ImageOps

from django.template import Library

register = Library()


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