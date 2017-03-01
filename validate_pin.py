__author__ = 'valeriy'

import re


def validate_pin(str):
    if re.match('^[0-9]{4}$', str) or re.match('^[0-9]{6}$', str):
        return True
    else:
        return False

p = validate_pin("a234")
print p