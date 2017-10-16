# coding: utf-8
from dartcms.utils.loading import get_model, is_model_registered

DARTCMS_REQUIRED_APPS = [
    'django_gravatar',
    'mptt',

    'dartcms',
    'dartcms.apps.filemanager',
    'dartcms.apps.modules',
    'dartcms.apps.users',
    'dartcms.apps.siteusers',
]

DARTCMS_OPTIONAL_APPS = [
    'dartcms.apps.sitesettings',
    'dartcms.apps.pages',
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

        if replacements:
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
