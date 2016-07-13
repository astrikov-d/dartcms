# coding: utf-8
from django.db import models
from django.utils.translation import ugettext as _

from .db import get_model_field_label, get_model_field_type


class DartCMSConfig(object):
    config = {}
    column_type_mapping = {
        models.DateTimeField: 'datetime',
        models.DateField: 'date',
        models.TimeField: 'time',
        models.BooleanField: 'boolean',
        models.ForeignKey: 'foreign_key'
    }
    default_action_label = _('View Records')
    default_action_icon = 'next'

    def __init__(self, config):
        self.config = config

    @property
    def base(self):
        return {
            'parent_kwarg_name': self.config.get('parent_kwarg_name'),
            'parent_model_fk': self.config.get('parent_model_fk'),
            'parent_model': self.config.get('parent_model'),
            'model': self.config.get('model'),
        }

    def construct_grid_columns(self):
        model = self.config['model']
        for column in self.config['grid']['grid_columns']:
            if 'label' not in column:
                column['label'] = get_model_field_label(model, column['field'])
            if 'type' not in column:
                column['type'] = self.column_type_mapping.get(get_model_field_type(model, column['field']), 'string')

    def construct_additional_grid_actions(self):
        for action in self.config['grid']['additional_grid_actions']:
            if 'label' not in action:
                action['label'] = self.default_action_label
            if 'icon' not in action:
                action['icon'] = self.default_action_icon

    @property
    def grid(self):
        config = self.base

        if config['model'] and 'grid_columns' in self.config['grid']:
            self.construct_grid_columns()

        if 'additional_grid_actions' in self.config['grid']:
            self.construct_additional_grid_actions()

        config.update(self.config['grid'])
        return config

    @property
    def form(self):
        config = self.base
        if 'form' in self.config:
            config.update(self.config['form'])
        return config
