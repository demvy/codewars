__author__ = 'valeriy'
"""
You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:

next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
"""

"""
ідеал спіжжений але також валиться на неінуванні підпослідовності для макса
def next_bigger(n):
    lst = list(str(n))
    print(lst)
    i = max(i for i in range(1, len(lst)) if lst[i - 1] < lst[i])
    j = max(j for j in range(i, len(lst)) if lst[j] > lst[i - 1])
    lst[j], lst[i - 1] = lst[i - 1], lst[j]
    print(lst, i - 1, j)
    lst[i:] = reversed(lst[i:])
    print(lst)
    return int(''.join(lst))
"""


def next_bigger(n):
    lst = list(str(n))
    lst.reverse()
    i = min(i for i in range(0, len(lst) - 1) if lst[i] > lst[i + 1])
    j = min(j for j in range(i, len(lst) - 1) if lst[j] > lst[i + 1])
    lst[i + 1], lst[j] = lst[j], lst[i + 1]
    lst[0: i + 1] = reversed(lst[0: i + 1])
    lst.reverse()
    return int(''.join(lst))


if __name__ == "__main__":
    print(next_bigger(1234567890))
    print(next_bigger(513))
    print(next_bigger(2017))
    print(next_bigger(414))
    print(next_bigger(144))