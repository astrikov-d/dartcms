# coding: utf-8
from django.db import models


def get_model_field_label(model, field_label):
    """
    Constructs label from model's field.
    """
    label = field_label.title()

    for field in model._meta.fields:
        column_field = field_label
        if isinstance(field, models.ForeignKey):
            column_field += '_id'

        if field.attname == column_field:
            label = getattr(field, 'verbose_name')
            if not label:
                label = field.attname.replace('_', '')
            break

    return label.title()


def get_model_field_type(model, field_label):
    """
    Returns model's field type.
    """
    for field in model._meta.fields:
        column_field = field_label
        if isinstance(field, models.ForeignKey):
            column_field += '_id'

        if field.attname == column_field:
            return type(field)
