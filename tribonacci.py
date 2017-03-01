__author__ = 'valeriy'


def tribonacci(signature, n):
    if n == 0:
        return []
    elif n < 0 or not isinstance(n, int):
        print("wrong n entered!")
        return 0
    else:
        for i in range(2, n - 1):
            signature.append(signature[i] + signature[i-1] + signature[i-2])
        return signature[:n]

tribonacci([0, 0, 1], 10)
