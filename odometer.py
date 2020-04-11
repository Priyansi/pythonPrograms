def convertToList(num: int) -> list:
    return [int(x) for x in str(num)]


def isValid(numberList: list) -> bool:
    return sorted(numberList) == numberList and list(sorted(set(numberList))) == numberList


def checkBorderConditions(currIndex: int, length: int) -> int:
    return length-abs(currIndex) if len(odometer) == currIndex or currIndex < 0 else currIndex


def findReadings(num: int, readings: int, direction: int, odometer: list) -> int:
    currIndex = odometer.index(num)
    readingsList = []
    while readings > 0:
        currIndex += 1*direction
        readings -= 1
        currIndex = checkBorderConditions(currIndex, len(odometer))
        readingsList.append(odometer[currIndex])
    return readingsList


def generateOdometer(size: int) -> list:
    return [int(x) for x in range(10**(size-1), 10**size) if isValid(convertToList(x))]


def calDistance(num1: int, num2: int, odometer: list):
    return odometer.index(num2)-odometer.index(num1) if num2 > num1 else len(odometer) - odometer.index(num2)-odometer.index(num1)


size = 4
firstNum = 6789
nextNum = 1234
readings = 10
direction = 1
odometer = generateOdometer(size)
print(findReadings(5789, readings, direction, odometer))
print(calDistance(firstNum, nextNum, odometer))
