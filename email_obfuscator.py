__author__ = 'valeriy'

import string


def obfuscate(email):
    if not isinstance(email, str):
        return 0
    else:
        email = string.replace(email, '@', ' [at] ')
        email = string.replace(email, '.', ' [dot] ')
        return email

a = obfuscate('jim.kuback@ennerman-hatano.com')
print(a)
