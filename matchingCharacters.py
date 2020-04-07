import sys


def matches(str1, str2):
    return sum((a == b) for a, b in zip(str1, str2))


print(matches(sys.argv[1], sys.argv[2]))
