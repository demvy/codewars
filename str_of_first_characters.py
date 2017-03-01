__author__ = 'valeriy'


def make_string(s):
    return ''.join([str(letter[0]) for letter in s.split(' ')])


a = make_string("sees eyes xray yoat")
print a