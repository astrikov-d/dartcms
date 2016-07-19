# coding: utf-8
import inspect
import importlib

from dartcms.utils.loading import get_model, is_model_registered

DARTCMS_REQUIRED_APPS = [
    'django_gravatar',
    'mptt',

    'dartcms',
    'dartcms.apps.filemanager',
    'dartcms.apps.modules',
    'dartcms.apps.pages',
    'dartcms.apps.sitesettings',
]

DARTCMS_OPTIONAL_APPS = [
    'dartcms.apps.ads',
    'dartcms.apps.feedback',
    'dartcms.apps.feeds',
    'dartcms.apps.shop',
]

DARTCMS_APPS = DARTCMS_REQUIRED_APPS + DARTCMS_OPTIONAL_APPS


def get_dartcms_core_apps(include_apps='*', replacements=None):
    """
    If you want to override default DartCMS app, you should pass your app labels (as iterable) to this function.

    Usage:

    INSTALLED_APPS = [
        ...
    ] + get_dartcms_core_apps(replacements=['your_project.pages'])

    This will override default DartCMS app named 'pages'.
    """
    if include_apps == '*' and not replacements:
        return DARTCMS_APPS

    def get_app_label(label):
        pattern = label.replace('dartcms.apps.', '')

        if isinstance(include_apps, (list, tuple)):
            if pattern not in include_apps:
                return

        for replacement in replacements:
            if replacement.endswith(pattern):
                return replacement
        return label

    apps = DARTCMS_REQUIRED_APPS
    for app_label in DARTCMS_OPTIONAL_APPS:
        app_label = get_app_label(app_label)
        if app_label:
            apps.append(app_label)

    return apps


def discover_models(app_label, existing_models):
    """
    Discovering models in certain app.
    If you want to override default DartCMS app, but you don't want to re-declare all models inside this app,
    you can call this function inside your custom app like this:

    Usage:

    # app: custom_app

    from django.db import models

    import dartcms

    from dartcms.apps.some_app.models import SomeAbstractModel


    __all__ = ['Model']

    __all__.extend(dartcms.discover_models('ads', __all__))


    class Model(SomeAbstractModel):
        custom_field = models.CharField(max_length=255)

    """
    from django.apps import apps
    from django.db import models

    caller = inspect.getmodule(inspect.stack()[1][0])
    module = importlib.import_module('dartcms.apps.%s.models' % app_label)

    m = []

    meta = type('Meta', (), {'app_label': app_label})

    for object_name in dir(module):
        klass = getattr(module, object_name)

        if inspect.isclass(klass) and issubclass(klass, models.Model):
            class_name = klass.__name__

            if class_name not in existing_models and class_name not in dir(caller):
                setattr(
                    caller,
                    class_name,
                    type(class_name, (klass, ), {
                        '__module__': app_label,
                        'Meta': meta
                    })
                )
                apps.register_model(app_label, getattr(caller, class_name))
                m.append(class_name)

    return m