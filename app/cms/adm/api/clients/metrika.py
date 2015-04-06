# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

import datetime
import requests
import json

from django.conf import settings


class Client(object):

    URL = 'http://api-metrika.yandex.ru/'

    def send_requests(self, ep, data, method="post"):
        headers = {
            'Authorization': 'OAuth %s' % settings.YANDEX_OAUTH_ACCESS_TOKEN,
            'Accept': 'application/x-yametrika+json',
            'Content-Type': 'application/x-yametrika+json',
        }

        methods = {
            "post": requests.post(self.URL + ep, data=json.dumps(data), headers=headers),
            "get": requests.get(self.URL + ep, params=data, headers=headers)
        }

        if method in methods:
            r = methods[method]
        else:
            r = None

        if r is not None:
            try:
                res = r.json()
                res['data'] = sorted(res['data'], key=lambda k: k['date'])
                return res
            except ValueError:
                print r
                return r.text
        else:
            return None

    def create_counter(self, site, name):
        """
        Create Y.Metrika counter.
        """
        data = {'counter': {'site': site, 'name': name}}
        return self.send_requests(ep='counters', data=data)

    def get_traffic(self, counter_id, date_start = None, date_end = None):
        """
        Get traffic for counter
        """
        data = {'id': counter_id}
        if date_start is not None and date_end is not None:
            data.update({
                'date1': datetime.datetime.strptime(date_start, "%d.%m.%Y").strftime("%Y%m%d"),
                'date2': datetime.datetime.strptime(date_end, "%d.%m.%Y").strftime("%Y%m%d")
            })
        return self.send_requests(ep='stat/traffic/summary', data=data, method="get")