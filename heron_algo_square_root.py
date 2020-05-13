import math


def sqrt(num, EPSILON=0.0000001):
    guess = 2
    r = 0.5*(guess+num/guess)
    while abs(guess-r) > EPSILON:
        guess = r
        r = 0.5*(guess+num/guess)
    return r


print(sqrt(123))
