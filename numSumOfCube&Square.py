import math


def cubes():
    return [i**3 for i in range(1, 10)]


def sumExpress(squareList, cubeList, num):
    for i in squareList:
        for j in cubeList:
            if i+j == num:
                return True
    return False


def squares() -> [int]:
    return [n for n in range(1, 1000) if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n))]


def qsqsq():
    squareList = squares()
    cubeList = cubes()
    return [i for i in squareList if sumExpress(squareList, cubeList, i)]


print(qsqsq())
