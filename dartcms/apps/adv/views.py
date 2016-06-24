# coding: utf-8
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from lib.utils.net import get_remote_addr

from .models import Click


class ClickView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        redirect_url = self.request.GET.get('redirect')
        ad_id = self.request.GET.get('id')

        if redirect_url and ad_id:
            Click.objects.create(
                ad_id=ad_id,
                url=redirect_url,
                referer=self.request.META.get('HTTP_REFERER'),
                ip_address=get_remote_addr(self.request),
                user_agent=self.request.META.get('HTTP_USER_AGENT')
            )
            return redirect_url
        return reverse_lazy("homepage")
