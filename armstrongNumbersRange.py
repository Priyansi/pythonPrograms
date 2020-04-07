import sys


def countDigits(num: int) -> int:
    return len(str(num))


def calculate(num: int) -> int:
    lenNum = countDigits(num)
    return sum([int(i)**lenNum for i in str(num)])


def armstrong(start: int, stop: int) -> list:
    return [x for x in range(start, stop+1) if calculate(x) == x]


print(armstrong(int(sys.argv[1]), int(sys.argv[2])))
