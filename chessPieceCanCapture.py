from chessCanMoveToPos import isPosInsideBoard, alphaPositions, pieceFunctions, king, queen, bishop, knight, rook


def pawnCapture(pos1, pos2):
    return int(pos2[1])-int(pos1[1]) == alphaPositions[pos2[0]]-alphaPositions[pos1[0]] == 1


def canPieceCapture(piece, pos1, pos2):
    if pos1 == pos2 or not(len(pos1) == len(pos2) == 2):
        return False
    if not isPosInsideBoard(pos1) or not isPosInsideBoard(pos2):
        return False
    if piece == 'p':
        return pawnCapture(pos1, pos2)
    if piece == 'P':
        return pawnCapture(pos2, pos1)
    return pieceFunctions[piece.lower()](pos1, pos2)


print(canPieceCapture('P', 'e5', 'd4'))
