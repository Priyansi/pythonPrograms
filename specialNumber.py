import sys


def convertList(num):
    return [int(x) for x in str(num)]


def factorial(n):
    return 1 if n == 1 else n*factorial(n-1)


def factorialListSum(n):
    return sum([factorial(x) for x in convertList(n)])


def IsSpecialNumber(n) -> bool:
    return factorialListSum(n) == n


print(IsSpecialNumber(sys.argv[1]))
