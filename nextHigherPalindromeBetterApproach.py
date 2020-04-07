# function that tests again cases, manipulates and finds the next palindrome
def nextPalindrome(number):
    length = len(str(number))
    leftHalf = getLeftHalf(number)
    middle = getMiddle(number)
    if number & 1:
        increment = pow(10, length//2)
        newNumber = int(leftHalf+middle+leftHalf[::-1])
    else:
        increment = int(1.1*pow(10, length//2))
        newNumber = int(leftHalf+leftHalf[::-1])
    if newNumber > number:
        return newNumber
    if middle != '9':
        return newNumber+increment
    else:
        return nextPalindrome(roundUp(number))


def getLeftHalf(number):
    return str(number)[:len(str(number))//2]


def getMiddle(number):
    return str(number)[(len(str(number))-1)//2]


def roundUp(number):
    length = len(str(number))
    increment = int(pow(10, ((length//2)+1)))
    return int(((number//increment)+1)*increment)


number = int(input())
print(nextPalindrome(number))
