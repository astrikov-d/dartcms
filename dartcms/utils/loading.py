# coding: utf-8
from importlib import import_module

from django.apps import apps
from django.apps.config import MODELS_MODULE_NAME
from django.conf import settings
from django.core.exceptions import AppRegistryNotReady


def get_model(app_label, model_name):
    try:
        return apps.get_model(app_label, model_name)
    except AppRegistryNotReady:
        if apps.apps_ready and not apps.models_ready:
            app_config = apps.get_app_config(app_label)
            import_module('%s.%s' % (app_config.name, MODELS_MODULE_NAME))
            return apps.get_registered_model(app_label, model_name)
        else:
            raise


def get_form_class(app_label, form_class_name):
    module = import_module('%s.%s' % (app_label, getattr(settings, 'FORMS_MODULE_NAME', 'forms')))
    return getattr(module, form_class_name)


def is_model_registered(app_label, model_name):
    try:
        apps.get_registered_model(app_label, model_name)
    except LookupError:
        return False
    else:
        return True
