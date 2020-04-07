import sys


def odd(n: int) -> bool:
    return n % 2 == 1


def nextTerm(p: int) -> int:
    return 3*p+1 if odd(p) else p//2


def series(start: int) -> [int]:
    if start == 4:
        return [4, 2, 1]
    else:
        return [start]+series(nextTerm(start))


print(series(int(sys.argv[1])))
