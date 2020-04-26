def isPrime(n):
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


def figSum(n):
    return sum([int(i) for i in str(n)])


def moranNumbers(n):
    total = figSum(n)
    if isPrime(n//total):
        return 'M'
    if n % total == 0:
        return 'H'
    return 'Neither'


print(moranNumbers(132))
