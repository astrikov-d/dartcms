# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

from types import NoneType
from django.db.models.manager import Manager
from django.db.models import Model
import datetime


def get_values(instance, go_into={}, exclude=(), extra=()):
    """
    Transforms a django model instance into an object that can be used for
    serialization. Also transforms datetimes into timestamps.

    @param instance(django.db.models.Model) - the model in question
    @param go_into(dict) - relations with other models that need expanding
    @param exclude(tuple) - fields that will be ignored
    @param extra(tuple) - additional functions/properties which are not fields

    Usage:
    get_values(MyModel.objects.get(pk=187),
               {'user': {'go_into': ('clan',),
                         'exclude': ('crest_blob',),
                         'extra': ('get_crest_path',)}},
               ('image'))

    """

    SIMPLE_TYPES = (int, long, str, list, dict, tuple, bool, float, bool,
                    unicode, NoneType)

    if not isinstance(instance, Model):
        raise TypeError("Argument is not a Model")

    value = {
        'pk': instance.pk,
    }

    # check for simple string instead of tuples
    # and dicts; this is shorthand syntax
    if isinstance(go_into, str):
        go_into = {go_into: {}}

    if isinstance(exclude, str):
        exclude = (exclude,)

    if isinstance(extra, str):
        extra = (extra,)

    # process the extra properties/function/whatever
    for field in extra:
        property = getattr(instance, field)

        if callable(property):
            property = property()

        if isinstance(property, SIMPLE_TYPES):
            value[field] = property
        else:
            value[field] = repr(property)

    field_options = instance._meta.get_all_field_names()
    for field in field_options:
        try:
            property = getattr(instance, field)
        except:
            continue

        if field in exclude or field[0] == '_' or isinstance(property, Manager):
            # if it's in the exclude tuple, ignore it
            # if it's a "private" field, ignore it
            # if it's an instance of manager (this means a more complicated
            # relationship), ignore it
            continue
        elif go_into.has_key(field):
            # if it's in the go_into dict, make a recursive call for that field
            try:
                field_go_into = go_into[field].get('go_into', {})
            except AttributeError:
                field_go_into = {}

            try:
                field_exclude = go_into[field].get('exclude', ())
            except AttributeError:
                field_exclude = ()

            try:
                field_extra = go_into[field].get('extra', ())
            except AttributeError:
                field_extra = ()

            value[field] = get_values(property,
                                      field_go_into,
                                      field_exclude,
                                      field_extra)
        else:
            if isinstance(property, Model):
                # if it's a model, we need it's PK #
                value[field] = property.pk
            elif isinstance(property, (datetime.date,
                                       datetime.time,
                                       datetime.datetime)):
                # if it's a date/time, we need it #
                # in iso format for serialization #
                value[field] = property.isoformat()
            else:
                # else, we just put the value #
                if callable(property):
                    property = property()

                if isinstance(property, SIMPLE_TYPES):
                    value[field] = property
                else:
                    value[field] = repr(property)

    return value


from django.core.exceptions import ObjectDoesNotExist


def model_to_dict(obj, exclude=['AutoField', 'ForeignKey', 'OneToOneField']):
    """
        serialize model object to dict with related objects

        author: Vadym Zakovinko <vp@zakovinko.com>
        date: January 31, 2011
        http://djangosnippets.org/snippets/2342/
    """
    tree = {}
    for field_name in obj._meta.get_all_field_names():
        try:
            field = getattr(obj, field_name)
        except (ObjectDoesNotExist, AttributeError):
            continue

        if field.__class__.__name__ in ['RelatedManager', 'ManyRelatedManager']:
            if field.model.__name__ in exclude:
                continue

            if field.__class__.__name__ == 'ManyRelatedManager':
                exclude.append(obj.__class__.__name__)
            subtree = []
            for related_obj in getattr(obj, field_name).all():
                value = model_to_dict(related_obj, exclude=exclude)
                if value:
                    subtree.append(value)
            if subtree:
                tree[field_name] = subtree

            continue

        field = obj._meta.get_field_by_name(field_name)[0]
        if field.__class__.__name__ in exclude:
            continue

        if field.__class__.__name__ == 'RelatedObject':
            exclude.append(field.model.__name__)
            tree[field_name] = model_to_dict(getattr(obj, field_name), exclude=exclude)
            continue

        value = getattr(obj, field_name)
        if value:
            tree[field_name] = value

    return tree