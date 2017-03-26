
"""
Consider the sequence a(1) = 7, a(n) = a(n-1) + gcd(n, a(n-1)) for n >= 2:

7, 8, 9, 10, 15, 18, 19, 20, 21, 22, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 69, 72, 73....

Let us take the differences between successive elements of the sequence and get a second sequence g: 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1....

For the sake of uniformity of the lengths of sequences we add a 1 at the head of g:

g: 1, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1...

Removing the 1s gives a third sequence: p: 5, 3, 11, 3, 23, 3... where you can see prime numbers.

Task:

Write functions:

1: an(n) with parameter n: returns the first n terms of the series a(n) (not tested)

2: gn(n) with parameter n: returns the first n terms of the series g(n) (not tested)

3: countOnes(n) with parameter n: returns the number of 1 in g(n)
    (don't forget to add a `1` at the head) # (tested)

4: p(n) with parameter n: returns an array of n unique prime numbers (not tested)

5: maxp(n) with parameter n: returns the biggest prime number of the sequence pn(n) # (tested)

6: anOver(n) with parameter n: returns an array (n terms) of the a(i)/i for every i such g(i) != 1 (not tested but interesting result)

7: anOverAverage(n) with parameter n: returns as an *integer* the average of anOver(n)  (tested)
Note:

You can write directly functions 3:, 5: and 7:. There is no need to write functions 1:, 2:, 4: 6: except out of pure curiosity.
"""
from fractions import gcd
from collections import Counter


def is_prime(a):
    return all(a % i for i in range(2, a))


def an(n):
    lst = [7]
    i = 1
    while i < n:
        lst.append(lst[i - 1] + gcd(i + 1, lst[i - 1]))
        i += 1
    return lst


def gn(n):
    lst = [1]
    a = an(n)
    lst.extend([a[i] - a[i - 1] for i, b in enumerate(a) if i > 0])
    return lst


def count_ones(n):
    return Counter(gn(n))[1]


def p(n):
    lst = list(set(list(filter((1).__ne__, gn(n * 20)))))
    return lst[:n]


def max_pn(n):
    #print(p(n))
    if len(p(n)):
        return max(p(n))
    else:
        return 2


def an_over(n):
    return [an(i)[-1]/i for i in range(2, n)]


def an_over_average(n):
    return round(sum(an_over(n)) / len(an_over(n)))

if __name__ == "__main__":
    print(an(14))
    #print(count_ones(10)) #8
    #print(count_ones(100)) #90
    print(max_pn(5))#, 47)
    print(max_pn(7)) #101)
    #print(an_over_average(5))#, 3)
