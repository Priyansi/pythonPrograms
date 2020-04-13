from string import ascii_lowercase as a_z
from string import ascii_uppercase as A_Z
ALPHABETS = a_z+a_z+A_Z+A_Z
n = 13


def convert(ch, n):
    if not ch.isalpha():
        return ch
    if n < 0:
        return ALPHABETS[ALPHABETS.rindex(ch)+n]
    return ALPHABETS[ALPHABETS.index(ch)+n]


def rotEncrypt(string):
    return ''.join([convert(ch, n) for ch in string])


print(rotEncrypt('this is a sentence'))
