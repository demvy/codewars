__author__ = 'valeriy'


def namelist(names):
    answer = ''
    value_list = []
    for i in names:
        value_list.append(i['name'])
    if len(value_list) == 0:
        answer = ''
    else:
        if len(value_list) > 1:
            answer = ', '.join([str(name) for name in value_list[:-1]]) + ' & ' + str(value_list[-1])
        else:
            answer = value_list[0]
    return answer


a = namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])
print a