# coding: utf-8
from django.utils.translation import get_language


def get_date_format():
    return {
        'ru-ru': '%d.%m.%Y',
        'en-us': '%Y-%m-%d'
    }.get(get_language())
