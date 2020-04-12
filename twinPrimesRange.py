from sys import argv


def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    elif n in [2, 3, 5, 7]:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        r = 5
        while r*r <= n:
            if n % r == 0:
                return False
            r += 2
            if n % r == 0:
                return False
            r += 4
        return True


def twinPrimesRange(start, end):
    if start <= 0 or end <= 0:
        return -1
    if start >= end:
        return -2
    a = [(i, i+2) for i in range(start, end-1) if isPrime(i) and isPrime(i+2)]
    return -3 if not len(a) else a


print(twinPrimesRange(int(argv[1]), int(argv[2])))
