# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

"""
Different functions for building hash-strings.
"""

import string
import random


def uuid():
    """
    Make unique hash.
    """

    import uuid

    return uuid.uuid1().hex


def random_string(symbols=6):
    """
    Make random string of specified len.
    """
    return ''.join(random.choice(string.digits) for i in range(symbols))