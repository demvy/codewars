
"""Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

"""


def dashatize(num):
    if isinstance(num, int):
        s = str(abs(num))
        res = ''
        for i in range(len(s)):
            if i != 0 and int(s[i]) % 2 == 1 and res[-1] != '-':
                res += '-'
            res += s[i]
            if i != len(s) - 1 and int(s[i]) % 2 == 1 and res[-1] != '-':
                res += '-'
        return res
    return 'None'


if __name__ == "__main__":
    print(dashatize(101))
    print(dashatize(274))
    print(dashatize(5311))
    print(dashatize(86320))
    print(dashatize(974302))