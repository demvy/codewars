__author__ = 'valeriy'


"""
Implement String#ipv4_address?, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading 0s, spaces etc.
"""

import re


def ipv4_address(address):
    if len(address.split('.')) != 4 or not re.match(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}\.\d{1,3}', address):
        return False
    lst = [str(x) for x in range(256)]
    for el in address.split('.'):
        if el not in lst:
            return False
    return True


if __name__ == "__main__":
    print(ipv4_address("")) #false
    print(ipv4_address("127.0.0.1")) #true
    print(ipv4_address("0.0.0.0"))# True)
    print(ipv4_address("255.255.255.255")) #, True)
    print(ipv4_address("10.20.30.40")) #, True)
    print(ipv4_address("10.256.30.40")) #, False)
    print(ipv4_address("10.20.030.40")) #, False)
    print(ipv4_address("127.0.1")) # False)
    print(ipv4_address("127.0.0.0.1")) #, False)
    print(ipv4_address("..255.255")) #, False)
    print(ipv4_address("127.0.0.1\n"))  #, False)
    print(ipv4_address("\n127.0.0.1")) #, False)
    print(ipv4_address(" 127.0.0.1")) #, False)
    print(ipv4_address("127.0.0.1 ")) #, False)
    print(ipv4_address(" 127.0.0.1 ")) #, False)