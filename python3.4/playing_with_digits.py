__author__ = 'valeriy'


def dig_pow(n, p):
    sum = 0
    for index, digit in enumerate(str(n)):
        sum += int(digit) ** (p + int(index))
    if sum % n == 0:
        return sum // n
    else:
        return -1

if __name__ == "__main__":
    print(dig_pow(46288, 3))