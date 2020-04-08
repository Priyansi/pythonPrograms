#  Generalized function for this -
#    *
#   ***
#  *****
# *******

import sys

space = ' '
asterisk = '*'


def spaces(x: int) -> str:
    return ''.rjust(x, space)


def asterisks(x: int) -> str:
    return ''.rjust(x, asterisk)


def pattern(num: int) -> str:
    return ''.join(spaces(num-(i-1))+asterisks((2*i)+1)+'\n' for i in range(num))


print(pattern(int(sys.argv[1])))
