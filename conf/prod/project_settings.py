__author__ = 'Dmitry Astrikov'

# Project and environment specific settings.

PROJECT_ROOT = '/var/www/example-domain.com'

APP_URL = "http://example-domain.com"

PORT = 80

DEBUG = False
PRODUCTION = True

DEFAULT_FROM_EMAIL = 'no-reply@example-domain.com'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

YM_COUNTER_ID = 26553798

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example_database',
        'USER': 'example_database_user',
        'PASSWORD': '*******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}