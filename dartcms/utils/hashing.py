# -*- coding: utf-8 -*-
import hashlib
import time


def md5(value=time.time()):
    return hashlib.md5(str(value)).hexdigest()
