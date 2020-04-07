ODD = 'O'
EVEN = 'E'


def checkOdd(array: int) -> bool:
    return array & 1


def is_solvable(loavesInHand: [int]) -> bool:
    return not checkOdd(sum(loavesInHand))


def numberToEO(num: int) -> str:
    return ODD if checkOdd(num) else EVEN


def convert(loaves: [int]) -> str:
    return ''.join([numberToEO(x) for x in loaves])


def rsolve(oeloaves: str) -> int:
    if oeloaves.count(ODD) == 0:
        return 0
    if oeloaves[0] == EVEN:
        return rsolve(oeloaves[1:])
    if oeloaves[0] == ODD and oeloaves[1] == ODD:
        return 2 + rsolve(oeloaves[2:])
    if oeloaves[0] == ODD and oeloaves[1] == EVEN:
        return 2 + rsolve(ODD + oeloaves[2:])


def solve(oeloaves: str) -> int:
    Es = oeloaves.split(ODD)
    relevantEs = Es[1::2]
    return sum([2*len(x)+2 for x in relevantEs])
