__author__ = 'valeriy'


def tax_calculator(total):
    if total <= 0 or not isinstance(total, int) and not isinstance(total, float):
        return 0
    else:
        if total <= 10:
            answer = (0.1 * total)
        elif total <= 20:
            answer = 1 + (total-10)*0.07
        elif total <= 30:
            answer = 1.7 + (total-20)*0.05
        else:
            answer = 2.2 + (total-30)*0.03
        return round(answer, 2)

b = tax_calculator(4.480973180691741)
print(b)
print type(b)
print(round(0.10, 2))