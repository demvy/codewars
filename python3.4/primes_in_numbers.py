__author__ = 'valeriy'

"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""
from math import sqrt
from collections import OrderedDict, Counter

def is_prime(a):
    return all(a % i for i in range(2, round(sqrt(a)) + 1))


def primeFactors(n):
    res = ''
    lst = list()
    for i in range(2, round(sqrt(n)) + 1):
        if i > n:
            break
        #print(i)
        if is_prime(i) and n % i == 0:
            #counter = 0
            while n % i == 0:
                #counter += 1
                lst.append(i)
                n //= i
            #if counter == 1:
            #    res += "(%d)" % i
            #else:
            #    res += "(%d**%d)" % (i, counter)
    c = dict((x, lst.count(x)) for x in set(lst))
    print(c)
    print("".join(["(" + str(k) + '**' + str(v) + ')' for k, v in c.items()]))
    #print(c)
    return res


if __name__ == "__main__":
    print(primeFactors(7775460))#== "(2**2)(3**3)(5)(7)(11**2)(17)")
    print(primeFactors(42547935335838392))