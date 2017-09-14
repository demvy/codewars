__author__ = 'valeriy'


def handle_numbers(number1, number2, number3):
    """
    :param number1: int number, start of interval
    :param number2: int number, enc of interval
    :param number3: divider
    :return: amount of numbers from number1 to number2
    """
    if not isinstance(number1, int) or not isinstance(number2, int):
        return 0
    return len([i for i in range(number1, number2 + 1) if not i % number3 and i != 0])


def handle_string(value):
    """
    :param value: string to search letters and digits in
    :return: dict with number of letters and digits in value
    """
    if not isinstance(value, str):
        return {'Letters': 0, 'Digits': 0}
    numbers = sum(char.isdigit() for char in value)
    words = sum(char.isalpha() for char in value)
    return {'Letters': words, 'Digits': numbers}


def handle_list_of_tuples(lst):
    """
    :param lst: list to sort
    :return: sorted list by 4 params
    """
    if not isinstance(lst, list):
        return []
    return sorted(lst, key=lambda e: (e[0], e[1], -int(e[2]), -int(e[3])))

