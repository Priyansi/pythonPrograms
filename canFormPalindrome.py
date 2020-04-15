def canFormPalindrome(string):
    def odd(ch):
        return string.count(ch) % 2 == 1
    return len(filter(odd, string)) <= 1


print(canFormPalindrome('palindrome'))
