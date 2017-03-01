__author__ = 'valeriy'


def calculate(num1, operation, num2):
    if not isinstance([num1, num2], int) and not isinstance([num1, num2], float) and operation not in ["+", "-", "*", "/"]:
        return None
    elif num1 is None or num2 is None:
        return -1
    else:
        if operation == "+":
            answer = num1 + num2
            return answer
        elif operation == "-":
            answer = num1 - num2
            return answer
        elif operation == "*":
            answer = num1 * num2
            return answer
        elif num2 != 0:
            answer = num1 / num2
            return answer
        else:
            return None


a = calculate(6, "-", 1.5)
print a
