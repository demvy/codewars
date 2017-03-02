__author__ = 'valeriy'

"""
Define a function

def last_digit(n1, n2):
  return
that takes in two numbers a and b and returns the last decimal digit of a^b. Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.

The inputs to your function will always be non-negative integers.

Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6
Remarks

JavaScript

Since JavaScript doesn't have native arbitrary large integers, your arguments are going to be strings representing non-negative integers, e.g.

lastDigit("10", "10000000000");
The kata is still as hard as the variants for Haskell or Python, don't worry.
"""


def last_digit(n1, n2):
    last = n1 % 10
    if last == 0 or last == 1 or last == 5 or last == 6:
        return last
    lst_4 = [6, 4]
    if last == 4:
        return lst_4[n2 % 2]
    lst_9 = [1, 9]
    if last == 9:
        return lst_9[n2 % 2]
    lst_3 = [3, 9, 7, 1]
    if last == 3:
        return lst_3[n2 % 4 - 1]
    lst_7 = [7, 9, 3, 1]
    if last == 7:
        return lst_7[n2 % 4 - 1]
    lst_2 = [2, 4, 8, 6]
    if last == 2:
        return lst_2[n2 % 4 - 1]
    lst_8 = [8, 4, 2, 6]
    return lst_8[n2 % 4 - 1]

if __name__ == "__main__":
    print(last_digit(4, 1)) #4
    print(last_digit(4, 2)) #6
    print(last_digit(9, 7)) #9
    print(last_digit(10, 10 ** 10)) #0
    print(last_digit(2 ** 200, 2 ** 300)) #6
    print(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651)) #7