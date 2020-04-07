def howMany(value, array):
    return array.count(value)


def sumByCount(array):
    total = 0
    for value in set(array):
        if howMany(value, array) == 1:
            total += value
    return total


array = list(map(int, input().split(' ')))
print(int(sumByCount(array)))
