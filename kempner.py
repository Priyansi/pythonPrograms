import math


def checkPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def kempner(n):
    if checkPrime(n):
        return n
    i = 1
    while math.factorial(i) % n >= 0:
        if math.factorial(i) % n == 0:
            return i
        i += 1


print(kempner(10))
