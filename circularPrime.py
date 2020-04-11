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


def circularStrings(num: int) -> str:
    length = len(str(num))
    for i in range(1, length):
        yield str(num)[i:]+str(num)[:i]


def hasDivisibleLastDigit(n: int) -> bool:
    return any([d in '024568' for d in str(n)])


def circularPrime(n: int):
    if n < 10:
        return isPrime(n)
    if hasDivisibleLastDigit(n):
        return False
    return all(isPrime(i) for i in circularStrings(n))


print(circularPrime(12))
