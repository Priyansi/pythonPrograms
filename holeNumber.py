dictionary = {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 0, 6: 1, 7: 0, 8: 2, 9: 1}


def calculateKey(i):
    return sum([dictionary[int(ch)] for ch in str(i)])


def sum_of_holes(limit):
    return sum([calculateKey(i+1) for i in range(limit)])
