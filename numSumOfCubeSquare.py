import math
import itertools

LIMIT = 1000
CUBE_LIMIT = math.ceil(LIMIT**0.33)
SQUARE_LIMIT = math.ceil(LIMIT**0.5)


def cubes() -> [int]:
    return [i**3 for i in range(1, CUBE_LIMIT+1)]


def squares() -> [int]:
    return [i**2 for i in range(1, SQUARE_LIMIT+1)]


def qsqsq():
    squareList = squares()
    cubeList = cubes()
    print(sorted(set(x+y for x, y in itertools.product(cubeList,
                                                       squareList) if x+y < LIMIT) & set(squareList)))


print(qsqsq())
