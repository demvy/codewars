__author__ = 'valeriy'


def first_chars(string):
    if not isinstance(string, str):
        return 0
    else:
        answer = ''
        word_list = string.split()
        for word in word_list:
            answer += word[0]
        return answer

b = first_chars('This Is A Test')
print b