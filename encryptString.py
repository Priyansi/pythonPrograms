import sys

dictionary = {'a': 0, 'e': 1, 'o': 2, 'u': 3}


def changeCharacter(ch):
    return str(dictionary[ch]) if ch in dictionary else ch


def newString(string):
    return ''.join(changeCharacter(x) for x in string)


def encrypt(string):
    return newString(string[::-1])+'aca'


print(encrypt(sys.argv[1]))
