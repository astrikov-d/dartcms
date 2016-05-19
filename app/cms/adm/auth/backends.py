# -*- coding: utf-8 -*-

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class AuthBackend(ModelBackend):
    user_model = User

    def authenticate(self, username=None, password=None, **kwargs):
        if 'subdomain' in kwargs and kwargs['subdomain'] == "admin":
            try:
                print 1
                user = self.user_model.objects.get(username=username, is_active=True, is_staff=True)
                if user.check_password(password):
                    return user
            except self.user_model.DoesNotExist:
                return None
            except ValueError:
                return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None