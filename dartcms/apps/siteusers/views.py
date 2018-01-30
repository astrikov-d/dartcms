from dartcms.apps.users.views import \
    ChangePasswordView as CMSChangePasswordView
from django.urls import reverse_lazy


class ChangePasswordView(CMSChangePasswordView):
    success_url = reverse_lazy('dartcms:siteusers:index')
