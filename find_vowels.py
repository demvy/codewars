__author__ = 'valeriy'

vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']


def vowel_indices(word):
    answer = []
    word_list = list(word)
    print word_list
    for letter in word_list:
        if letter in vowel_list:
            answer.append(int(word_list.index(letter)))
        else:
            continue
    return answer


a = vowel_indices("vowel_indices")
print a