# -*- coding: utf-8 -*-
__author__ = 'Dmitry Astrikov'

"""
Different functions for building hash-strings.
"""

import string
import random
import hashlib
import time


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




class Hash():
    def sha1(self, value):
        """
        Make a sha1 hash of the value.
        :param value:
        :return:
        """
        return hashlib.sha1(value).hexdigest()

    @staticmethod
    def md5(value=time.time()):
        """
        Make a md5 from the value.
        :param value:
        :return:
        """
        return hashlib.md5(str(value)).hexdigest()

    def uuid_hex(self):
        """
        Make a random uuid
        :return:
        """
        import uuid

        return uuid.uuid1().hex