# coding: utf-8
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class DartCMSAuthBackend(ModelBackend):
    user_model = User

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = self.user_model.objects.get(username=username, is_active=True, is_staff=True)
            if user.check_password(password):
                return user
        except self.user_model.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_model.objects.get(pk=user_id)
        except self.user_model.DoesNotExist:
            return None
