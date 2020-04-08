#  Generalized function for this with 4 orientations-
#         #
#        #-#
#       #---#
#      #-----#

from sys import argv

HASH, SPACE, HYPHEN = "#", ' ', '-'
LF, BACKSPACE = "\n", '\b'
SCREEN_WIDTH = 60

SP = HASH
RP = HYPHEN+HYPHEN
EP = BACKSPACE+HASH

#ORIENTATIONS = 'RIGHT', 'PYRAMID', 'INVERSE', 'DIAMOND'


def pattern(size: int, orientation='PYRAMID', width=SCREEN_WIDTH):
    if orientation == 'PYRAMID':
        return LF.join([line(line_no, width) for line_no in range(size)])
    elif orientation == 'RIGHT':
        return LF.join([line(line_no, 0) for line_no in range(size)])
    elif orientation == 'DIAMOND':
        return LF.join([line(line_no, width) for line_no in range(size)])+LF+LF.join([line(line_no, width) for line_no in range(size-1)][::-1])

    else:  # orientation =="INVERSE"
        return LF.join([line(line_no, width) for line_no in range(size)][::-1])


def line(n: int, width: int) -> str:
    return leading_space(n, width)+start_pattern(n)+repeat_pattern(n)+end_pattern(n)


def leading_space(n: int, w: int) -> str:
    return (w // 2 - n) * SPACE


def start_pattern(n: int):
    return SP


def repeat_pattern(n: int):
    return n*RP


def end_pattern(n: int):
    return EP


print(pattern(int(argv[1]), argv[2]))
