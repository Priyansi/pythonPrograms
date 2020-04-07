import sys
import math

START, LIMIT = 1000, 10000


def allDigitsEven(num: int) -> bool:
    return not 1 in [int(x) & 1 for x in str(num)]


def perfectSquare(num: int) -> bool:
    squareRoot = math.sqrt(num)
    return math.ceil(squareRoot) == math.floor(squareRoot)


def numberList() -> list:
    return [num for num in range(START, LIMIT) if allDigitsEven(num) and perfectSquare(num)]


print(numberList())
