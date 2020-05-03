from chessCanMoveToPos import isPosInsideBoard, alphaToNum, pieceFunctions, king, queen, bishop, knight, rook


def pawnCapture(pos1, pos2):
    return int(pos2[1])-int(pos1[1]) == 1 and abs(alphaToNum[pos2[0]]-alphaToNum[pos1[0]]) == 1


def canPieceCapture(piece, pos1, pos2):
    if pos1 == pos2 or not(len(pos1) == len(pos2) == 2):
        return False
    if not isPosInsideBoard(pos1) or not isPosInsideBoard(pos2):
        return False
    if piece == 'P':
        return pawnCapture(pos1, pos2)
    if piece == 'p':
        return pawnCapture(pos2, pos1)
    return pieceFunctions[piece.lower()](pos1, pos2)


if __name__ == "__main__":
    print(canPieceCapture('p', 'c5', 'd4'))
