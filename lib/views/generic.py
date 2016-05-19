# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import json

from django.core.serializers.json import DjangoJSONEncoder
from django.views.generic import View
from django.http import HttpResponse, HttpResponseBadRequest


class AjaxRequestView(View):
    """
    Simple ajax response view.
    """

    def get_response(self, request, *args, **kwargs):
        """
        You should redefine this method.
        """
        return {}

    def process_request(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        response = self.get_response(request, *args, **kwargs)
        return self.send_response(response)

    def get(self, request, *args, **kwargs):
        return self.process_request(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.process_request(request, *args, **kwargs)

    def send_response(self, response):
        return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='text/html')