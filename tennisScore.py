SETS = {'A': 0, 'B': 0}
CURRGAME = {'A': 0, 'B': 0}
CURRPOINTS = {'A': 0, 'B': 0}
POINTS = {'A': 0, 'B': 0}
POINTSDICT = {0: 0, 1: 15, 2: 30, 3: 40}
adv = ''
tie = False


def otherCharacter(i):
    return 'B' if i == 'A' else 'A'


def checkSetWon(i):
    global CURRGAME, tie
    j = otherCharacter(i)
    if CURRGAME[i] - CURRGAME[j] >= 2:
        return True
    elif CURRGAME[i] == CURRGAME[j] == 6:
        tie = True
        return False
    elif tie == True:
        tie = False
        return True
    else:
        return False


def checkGameWon(i):
    global CURRPOINTS, SETS, CURRGAME, adv, POINTS
    j = otherCharacter(i)
    if POINTS[i] < 3:
        POINTS[i] += 1
        CURRPOINTS[i] = POINTSDICT[POINTS[i]]
    else:
        if adv == j:
            adv = ''
        elif adv == i or POINTS[i] > POINTS[j]:
            CURRGAME[i] += 1
            if CURRGAME[i] >= 6 and checkSetWon(i):
                SETS[i] += 1
                CURRGAME = dict.fromkeys(CURRGAME, 0)
            CURRPOINTS = dict.fromkeys(CURRPOINTS, 0)
            POINTS = dict.fromkeys(POINTS, 0)
            adv = ''
        else:
            adv = i


def calculatePoints(string):
    for i in string:
        checkGameWon(i)


def printDict(dictionary):
    return ''.join(str(dictionary[i])+' ' for i in dictionary)


calculatePoints('ABABABAA')
print("player : A B"+"\nsets : "+printDict(SETS)+"\ngame : " +
      printDict(CURRGAME)+"\npoints : "+printDict(CURRPOINTS))
