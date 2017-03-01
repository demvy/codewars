__author__ = 'valeriy'


def insert_dash2(num):
    num = list(str(num))
    answer = ''
    for index, obj in enumerate(num):
        previous = num[index - 1]
        if (index==0)or(int(obj)==0)or(int(previous)==0):
            answer += obj
            continue
        elif (int(obj)%2==0 and int(previous)%2==0):
            answer += '*'+ obj
        elif (int(obj)%2!=0 and int(previous)%2!=0):
            answer += '-' + obj
        else:
            answer += obj
            continue

    return answer