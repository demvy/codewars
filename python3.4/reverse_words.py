__author__ = 'valeriy'

"""
Write a reverseWords function that accepts a string a parameter, and reverses each word in the string. Every space should stay, so you cannot use words from Prelude.

Example:

reverse_words("This is an example!") # returns  "sihT si na !elpma
"""


def reverse_words(str):
    return ' '.join([word[:: -1] for word in str.split(' ')])


if __name__ == "__main__":
    print(reverse_words('This is an example!'))