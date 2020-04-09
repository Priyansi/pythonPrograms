def isPrime(n: int) -> bool:
    if n in [2, 3, 5, 7]:
        return True
    elif n % 2 == 0 or n == 1:
        return False
    else:
        r = 3
        while r*r <= n:
            if n % r == 0:
                return False
            r += 2
        return True


def circularStrings(num: int) -> list:
    length = len(str(num))
    return [int(str(num)[i:]+str(num)[:i]) for i in range(length)]


def circularPrime(num: int):
    return not False in[isPrime(i) for i in circularStrings(num)]


print(circularPrime(1))
