def reverse(string: str):
    return string[::-1]


def convertToBinary(n: int):
    return bin(n).replace('0b', '')


def isDoubleBasePalindrome(n):
    binary = convertToBinary(n)
    return reverse(str(n)) == str(n) and reverse(binary) == binary


print(isDoubleBasePalindrome(585))
