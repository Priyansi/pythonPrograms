# INPUT - $-3x^2 + x - 7$
# OUTPUT - $-7 +x -3x^2$
import re

PLUS = '+'
MINUS = '-'
SPACE = ' '
DOLLAR = '$'
EMPTY_STRING = ''


def convert_to_common_pattern(poly):
    return poly.replace(PLUS, SPACE+PLUS).replace(MINUS, SPACE+MINUS)


def reverse_poly(poly):
    common_pattern = convert_to_common_pattern(
        poly.strip(DOLLAR).replace(SPACE, EMPTY_STRING))
    return DOLLAR + SPACE.join(common_pattern.split(SPACE)[::-1]).strip(PLUS+SPACE) + DOLLAR


print(reverse_poly('$-3  x  ^    2 + x - 7   $'))
