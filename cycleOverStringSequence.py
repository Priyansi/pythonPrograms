import itertools


def nextCharacters(string, c):
    character = itertools.cycle(string)
    return ''.join(next(character) for i in range(c+1))[-1]


def pick10(s: str, n: int) -> str:
    count = 0
    word = ''
    seq = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    while count < 10:
        word += nextCharacters(s[n:]+s[:n], seq[count])
        count += 1
    return word


print(pick10('ABC', 1))
