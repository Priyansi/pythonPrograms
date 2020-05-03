alphaToNum = {'a': 1, 'b': 2, 'c': 3,
              'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
whiteHome = 2
blackHome = 7


def rook(pos1, pos2):
    return pos1[0] == pos2[0] or pos1[1] == pos2[1]


def bishop(pos1, pos2):
    return abs(alphaToNum[pos1[0]]-alphaToNum[pos2[0]]) == abs(int(pos1[1])-int(pos2[1]))


def knight(pos1, pos2):
    return (abs(int(pos1[1])-int(pos2[1])), abs(alphaToNum[pos1[0]]-alphaToNum[pos2[0]])) in [(1, 2), (2, 1)]


def queen(pos1, pos2):
    return bishop(pos1, pos2) or rook(pos1, pos2)


def king(pos1, pos2):
    return (abs(alphaToNum[pos1[0]]-alphaToNum[pos2[0]]), abs(int(pos1[1])-int(pos2[1]))) in [(0, 1), (1, 0), (1, 1)]


def pawn(pos1, pos2):
    return int(pos2[1])-int(pos1[1]) == 1 and pos1[0] == pos2[0]


def pawnWhite(pos1, pos2):
    if (int(pos1[1]), int(pos2[1])) == (whiteHome, whiteHome+2) and pos1[0] == pos2[0]:
        return True
    return pawn(pos1, pos2)


def pawnBlack(pos1, pos2):
    if (int(pos1[1]), int(pos2[1])) == (blackHome, blackHome-2) and pos1[0] == pos2[0]:
        return True
    return pawn(pos2, pos1)


def isPosInsideBoard(pos):
    return pos[0] in alphaToNum and int(pos[1]) in alphaToNum.values()


pieceFunctions = {'k': king, 'q': queen,
                  'n': knight, 'r': rook, 'b': bishop}


def isMoveValid(piece, pos1, pos2):
    if pos1 == pos2 or not(len(pos1) == len(pos2) == 2):
        return False
    if not isPosInsideBoard(pos1) or not isPosInsideBoard(pos2):
        return False
    if piece == 'p':
        return pawnBlack(pos1, pos2)
    if piece == 'P':
        return pawnWhite(pos1, pos2)
    return pieceFunctions[piece.lower()](pos1, pos2)


if __name__ == "__main__":
    print(isMoveValid('P', 'd2', 'd4'))
