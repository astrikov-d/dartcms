# coding: utf-8
import importlib
from django.db import models


DARTCMS_CORE_APPS = [
    'dartcms',
    'dartcms.apps.ads',
    'dartcms.apps.modules',
    'dartcms.apps.pages',
]


def get_dartcms_core_apps(replacements=None):
    """
    If you want to override default DartCMS app, you should pass your app labels (as iterable) to this function.
    Usage:

    INSTALLED_APPS = [
        ...
    ] + get_dartcms_core_apps(['your_project.pages'])

    This will override default DartCMS app named 'pages'.
    """
    if not replacements:
        return DARTCMS_CORE_APPS

    def get_app_label(label, replacements):
        pattern = label.replace('dartcms.apps.', '')
        for replacement in replacements:
            if replacement.endswith(pattern):
                return replacement
        return label

    apps = []
    for app_label in DARTCMS_CORE_APPS:
        apps.append(get_app_label(app_label, replacements))

    return apps


def create_models(app_label):
    """
    Example how to redefine abstract module in your app's models

    from django.db import models
    from dartcms.apps.ads.models import AbstractAd
    from dartcms import create_models

    __all__ = [
        'Ad'
    ]

    [__all__.append(i) for i in create_models('ads')]

    class Ad(AbstractAd):
        bar_field = models.CharField(max_length=255)

    """
    prep = []
    module = importlib.import_module('dartcms.apps.%s.models' % app_label)
    objects = dict([(name, cls) for name, cls in module.__dict__.items() if isinstance(cls, models.Model)])
    [prep.append(name) for name, cls in objects.items()]
    return prep
