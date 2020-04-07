import sys


def digitalRoot(num):
    return num % 9 if num % 9 else 9


print(digitalRoot(int(sys.argv[1])))
