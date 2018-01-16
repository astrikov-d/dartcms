# coding: utf-8
from dartcms.utils.loading import get_model
from django.conf import settings


def get_user_model():
    app_label, model_name = getattr(settings, 'AUTH_USER_MODEL', 'auth.User').split('.')
    return get_model(app_label, model_name)
