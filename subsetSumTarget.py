import itertools


def removeLargerNumThanK(n: list, k: int) -> list:
    return [i for i in n if i <= k]


def generateSubsets(n: list) -> list:
    for i in range(1, len(n)):
        for j in itertools.combinations(n, i):
            yield list(j)


def checkCondition(sublist: list, k: int) -> bool:
    return sum(sublist) == k


def checkSubestSum(n: int, k: int) -> list:
    return [i for i in generateSubsets(n) if checkCondition(i, k)]


n = list(map(int, input().split()))
k = int(input())
n = removeLargerNumThanK(n, k)
print(checkSubestSum(n, k))
