# -*- coding: utf-8 -*-
# Django settings for charm project.

import os

from project_settings import *
from conf.etc.apps import *
from conf.etc.yandex import *

SITE_ID = 1

ADMIN_APP_SUBDOMAIN = "admin"

TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'www/data')
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'www/static')

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'app/locale'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "tpl"),
)

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Krasnoyarsk'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/data/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xit&zie=_ujn+@7664)+zbq71$u*ff!gfd^ykavm2#@-s$!nok'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'lib.processors.context.template_variables',
    'lib.processors.adm.context.template_variables'
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'lib.middleware.page.PageMiddleware'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # https://github.com/django-debug-toolbar/django-debug-toolbar
    'debug_toolbar',
    # https://pypi.python.org/pypi/django-widget-tweaks
    'widget_tweaks',
    # https://pypi.python.org/pypi/django-gravatar2
    'django_gravatar',
    # https://github.com/etianen/django-watson/wiki
    'watson',

    # Lib
    'lib',
) + PROJECT_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Django debug toolbar configuration
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
DEBUG_TOOLBAR_PATCH_SETTINGS = False

DATE_INPUT_FORMATS = (
    '%d.%m.Y'
)

DATETIME_INPUT_FORMATS = (
    '%d.%m.Y %H:%M:%S'
)

# Trailing slash
APPEND_SLASH = True

SESSION_SAVE_EVERY_REQUEST = True

ROOT_URLCONF = 'app.site.urls'

SUBDOMAIN_URLCONFS = {
    None: 'app.site.urls',
    'www': 'app.site.urls',
    'dev': 'app.site.urls',
    'admin': 'app.adm.urls',
}

AUTHENTICATION_BACKENDS = (
    'lib.backends.adm.auth.AuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_URL = 'login'