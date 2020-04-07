def calculateTrace(array):
    trace = 0
    for i in range(len(array)):
        trace += array[i][i]

    return str(trace)


def calculateRows(array):
    n = len(array[0])
    numberRows = 0
    for i in array:
        if len(set(i)) != n:
            numberRows += 1

    return str(numberRows)


def calculateColumns(array):
    n = len(array[0])
    numberColumns = 0
    for i in range(n):
        columnList = [array[j][i] for j in range(n)]
        if len(columnList) != len(set(columnList)):
            numberColumns += 1

    return str(numberColumns)


t = int(input())
dictionary = {}
counter = 1
for x in range(t):
    n = int(input())
    dictionary[counter] = []
    for y in range(n):
        dictionary[counter].append(list(map(int, input().strip().split(' '))))
    counter += 1

for key in dictionary:
    print('Case #'+str(key)+': '+calculateTrace(dictionary[key])+' ' +
          calculateRows(dictionary[key])+' '+calculateColumns(dictionary[key]))
