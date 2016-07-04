# coding: utf-8
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