# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'


def get_list_of_errors(form):
    errors = {}
    for k in form.errors:
        errors[k] = form.errors[k][0]
    return errors