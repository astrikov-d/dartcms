# coding: utf-8
from dartcms.views import (DeleteMultipleObjectView, DeleteObjectView,
                           GridView, InsertObjectView,
                           InsertObjectWithInlinesView, UpdateObjectView,
                           UpdateObjectWithInlinesView)
from django.conf.urls import include, url
from django.forms import modelform_factory
from django.utils.translation import ugettext as _

from .db import get_model_field_label, get_model_field_type


class DartCMSConfig(object):
    config = {}

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
                column['type'] = get_model_field_type(model, column['field'])

    def construct_additional_grid_actions(self):
        for action in self.config['grid']['additional_grid_actions']:
            if 'label' not in action:
                action['label'] = self.default_action_label
            if 'icon' not in action:
                action['icon'] = self.default_action_icon

    @property
    def grid(self):
        config = self.base

        if config['model']:
            if 'grid_columns' in self.config['grid']:
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
        elif config.get('model'):
            config['form_class'] = modelform_factory(config['model'], exclude=[])
        return config

    def get_urls(self, exclude=None):
        if exclude is None:
            exclude = []
        urls = []

        if 'index' not in exclude:
            urls += [url(r'^$', GridView.as_view(**self.grid), name='index')]

        if 'insert' not in exclude:
            insert_view = InsertObjectWithInlinesView if 'inlines' in self.form else InsertObjectView
            urls += [url(r'^insert/$', insert_view.as_view(**self.form), name='insert')]

        if 'update' not in exclude:
            update_view = UpdateObjectWithInlinesView if 'inlines' in self.form else UpdateObjectView
            urls += [url(r'^update/(?P<pk>\d+)/$', update_view.as_view(**self.form), name='update')]

        if 'delete' not in exclude:
            if not self.grid.get('single_select', True):
                urls += [
                    url(r'^delete/(?P<pks>[\d,]+)/$', DeleteMultipleObjectView.as_view(**self.base), name='delete')]
            else:
                urls += [url(r'^delete/(?P<pk>\d+)/$', DeleteObjectView.as_view(**self.base), name='delete')]

        if 'addition' not in exclude and 'additional_grid_actions' in self.grid:
            for action in self.grid.get('additional_grid_actions', []):
                if 'kwarg_name' in action:
                    pattern = r'^(?P<children_url>{url})/(?P<{kwarg_name}>\d+)/'
                else:
                    pattern = r'^(?P<children_url>{url})/(?P<{kwarg_name}>\d+)/'

                if 'include_urls' in action:
                    urls += [url(pattern.format(**action),
                                 include(action['include_urls'], namespace=action['url']))]
                else:
                    urls += [url(pattern.format(**action), action['view'], name=action['url'])]

        return urls
