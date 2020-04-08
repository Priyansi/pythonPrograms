#  Generalized function for this -
#    *
#   ***
#  *****
# *******

import sys

space = ' '
asterisk = '*'


def spaces(x: int) -> str:
    return x*space


def asterisks(x: int) -> str:
    return x*asterisk


def checkEndLine(x: int) -> str:
    return '\n' if x else ''


def pattern(num: int) -> str:
    return ''.join(spaces(num-i-1)+asterisks((2*i)+1)+checkEndLine(num-i-1) for i in range(num))


print(pattern(int(sys.argv[1])))
