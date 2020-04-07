#  Generalized function for this -
#    *
#   ***
#  *****
# *******

import sys


def spaces(x: int) -> str:
    return ''.rjust(x, ' ')


def pattern(num: int) -> str:
    return ''.join(spaces(num-i-1)+''.rjust(i*2+1, '*')+'\n' for i in range(num))


print(pattern(int(sys.argv[1])))
