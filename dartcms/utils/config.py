# coding: utf-8
class DartCMSConfig(object):
    config = {}

    def __init__(self, config):
        self.config = config

    @property
    def base(self):
        return {
            'parent_kwarg_name': self.config.get('parent_kwarg_name'),
            'parent_model_fk': self.config.get('parent_model_fk'),
            'parent_model': self.config.get('parent_model'),
            'model': self.config['model'],
        }

    @property
    def grid(self):
        config = self.base
        config.update(self.config['grid'])
        return config

    @property
    def form(self):
        config = self.base
        config.update(self.config['form'])
        return config
