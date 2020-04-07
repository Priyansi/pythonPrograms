import sys

classificationList = ['Alpha', 'Gamma', 'Beta']


def calculateIndex(diff):
    if diff == 0:
        return 0
    return diff//abs(diff)


def aliquotSum(n):
    return sum([x for x in range(1, n//2 + 1) if n % x == 0])


def classify(n):
    return classificationList[calculateIndex(int(n) - aliquotSum(int(n))) + 1]


print(classify(sys.argv[1]))
