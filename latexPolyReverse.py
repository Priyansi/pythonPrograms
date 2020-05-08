# INPUT - $-3x^2 + x - 7$
# OUTPUT - $-7 +x -3x^2$
import re


def convert_to_common_pattern(poly):
    return poly.replace('+', ' +').replace('-', ' -')


def reverse_poly(poly):
    common_pattern = convert_to_common_pattern(
        poly.strip('$').replace(' ', ''))
    return '$'+' '.join(common_pattern.split(' ')[::-1]).strip('+ ')+'$'


print(reverse_poly('$-3  x  ^    2 + x - 7   $'))
