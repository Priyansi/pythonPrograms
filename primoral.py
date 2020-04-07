import sys
import math
import numpy


def checkPrime(n) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def firstN(number):
    START = 2
    listPrimes = []
    for i in range(1, number+1):
        while not checkPrime(START):
            START += 1
        listPrimes.append(START)
        START += 1

    return listPrimes


def getPrimoral(number):
    return numpy.prod(firstN(number))


print(getPrimoral(3))
