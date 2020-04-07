import sys
START, LIMIT = int(sys.argv[1]), int(sys.argv[2])


def make_armstrong(a: int, b: int) -> [int]:
    return [x for x in range(a, b) if is_armstrong(x)]


def is_armstrong(n: int) -> bool:
    return n == sum(cubes(digits(n)))


def cubes(ds: int) -> int:
    return [d**len(ds) for d in ds]


def digits(n: int) -> [int]:
    return [int(ch) for ch in str(n)]


print(make_armstrong(START, LIMIT))
