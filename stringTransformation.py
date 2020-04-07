def isValid(string: str) -> bool:
    return not (string.count('1')+string.count('0')) == (string.count('A')+string.count('B')+string.count('C') + 1)


def convertStringToList(string) -> list:
    return [x for x in string]


def evaluate(string):
    stringList = convertStringToList(string)

    if isValid(string):
        return -1
    for x in range(0, len(stringList)-1, 2):

        if stringList[x+1] == 'A':
            stringList[x+2] = str(stringList[x] and stringList[x+2])

        elif stringList[x+1] == 'B':
            stringList[x+2] = str(stringList[x] or stringList[x+2])

        elif stringList[x+1] == 'C':
            stringList[x+2] = str(int(stringList[x]) ^ int(stringList[x+2]))

    return stringList[-1]


string = input()
print(evaluate(string))
