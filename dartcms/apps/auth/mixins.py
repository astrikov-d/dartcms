# coding: utf-8
from django.contrib.auth.mixins import UserPassesTestMixin


class StaffRequiredMixin(UserPassesTestMixin):
    login_url = 'dartcms:auth:login'

    def test_func(self):
        return self.request.user.is_staff
