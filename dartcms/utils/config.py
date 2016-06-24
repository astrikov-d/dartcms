# coding: utf-8
class DartCMSConfig(object):
    config = {}

    def __init__(self, config):
        self.config = config

    @property
    def base(self):
        return {
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
