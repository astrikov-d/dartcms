from django.core.urlresolvers import reverse_lazy
from dartcms.apps.users.views import ChangePasswordView as CMSChangePasswordView


class ChangePasswordView(CMSChangePasswordView):
    success_url = reverse_lazy('dartcms:siteusers:index')
