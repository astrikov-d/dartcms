__author__ = 'Dmitry Astrikov'

# Project and environment specific settings.

PROJECT_ROOT = '/var/www/dartcms'

APP_URL = "http://dartcms.dev:8000"

PORT = 8000

DEBUG = True
PRODUCTION = False

DEFAULT_FROM_EMAIL = 'no-reply@dartcms.dev'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

YM_COUNTER_ID = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dartcms',
        'USER': 'dartcms',
        'PASSWORD': '********',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}