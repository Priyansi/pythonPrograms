import sys


def factorialTrailingZeros(num: int) -> int:
    count = 0
    i = 5
    while num//i:
        count += num//i
        i *= 5
    return count


print(factorialTrailingZeros(int(sys.argv[1])))
