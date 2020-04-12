import sys

SMALL = "abcdefghijklmnopqrstuvwxyz"
CAPITAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def convert(ch):
    if ch in SMALL:
        return SMALL[(SMALL.find(ch)+13) % 26]
    if ch in CAPITAL:
        return CAPITAL[(CAPITAL.find(ch)+13) % 26]
    else:
        return ch


def rot13(string):
    return ''.join([convert(ch) for ch in string])


print(rot13(sys.argv[1]))
