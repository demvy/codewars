__author__ = 'valeriy'

import re


def validate(email):
    if not re.match(r"^[A-Za-z]+[A-Za-z0-9\.\+_]+@[A-Za-z0-9\.+_-]+\.[a-zA-Z]*$", email):
        return False
    else:
        return True