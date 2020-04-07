# function that incremets and checks palindrome
def palindrome(number: int) -> int:
    while True:
        if str(number) == str(number)[::-1]:
            return number
        else:
            number += 1


number = int(input())
print(palindrome(number))
