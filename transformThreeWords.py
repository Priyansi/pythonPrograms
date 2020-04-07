import sys


def firstWord(first: str) -> str:
    convertedFirst = ''
    for ch in first:
        convertedFirst += '$' if ch in 'AEIOU' else ch

    return convertedFirst


def secondWord(second: str) -> str:
    convertedSecond = ''
    for ch in second:
        convertedSecond += '#' if ch in 'BCDFGHJKLMNPQRSTVWXYZ' else ch

    return convertedSecond


def thirdWord(third: str) -> str:
    return third.upper()


def stringTransformation(array):
    return firstWord(array[0])+secondWord(array[1])+thirdWord(array[2])


print(stringTransformation(['priyansi', 'himan*si', 'kiSHORW']))
