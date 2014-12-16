__author__ = 'Dmitry Astrikov'

# Project and environment specific settings.

PROJECT_ROOT = '/var/www/project_root'

APP_URL = "http://project-domain.dev"

PORT = 8000

DEBUG = True

DEFAULT_FROM_EMAIL = 'no-reply@project-domain.dev'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

YM_COUNTER_ID = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project-db-name',
        'USER': 'project-db-user',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}