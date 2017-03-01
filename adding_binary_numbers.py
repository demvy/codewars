__author__ = 'valeriy'


def add(bin1, bin2):
    if not isinstance(bin2, str) or not isinstance(bin1, str):
        return 0
    else:
        answer = ''
        for i in range(0, max(len(bin1), len(bin2))):
            if bin1[i] is not None and bin2[i] is None:
                answer += bin

            if bin1[i] == 1 and bin2[i] == 1:
                answer += '1' + str((int(bin1[i])+int(bin2[i])) % 2)
            else:
                answer += str((int(bin1[i])+int(bin2[i])) % 2)
        return answer


def adding(bin1, bin2):
    if not isinstance(bin2, str) or not isinstance(bin1, str):
        return 0
    else:
        answer = []
        bin1 = list(bin1)
        bin2 = list(bin2)
        for i in reversed(range(min(len(bin1), len(bin2)))):
            answer[i] = str((int(bin1[i])+int(bin2[i])) % 2)
            if bin1[i] == 1 and bin2[i] == 1 and i != 0:
                bin1[i+1] = str((int(bin1[i+1])+1) % 2)
            elif bin1[i] == 1 and bin2[i] == 1 and i == 0:
                answer[i+1] = "1"
        return answer

a = adding('111', '10')
print a