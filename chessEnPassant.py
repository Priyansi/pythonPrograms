from chessCanMoveToPos import alphaToNum


def is_en_passant(piece, sqaure_at, square_to_go):
    if sqaure_at[0] == square_to_go[0]:
        if (piece, sqaure_at[1], square_to_go[1]) == ('P', '2', '4'):
            return True
        if (piece, sqaure_at[1], square_to_go[1]) == ('p', '7', '5'):
            return True
    return False


def can_capture_en_passant(piece, square_en_passant, pos1, pos2):
    file_difference = abs(alphaToNum[pos1[0]]-alphaToNum[pos2[0]])
    if file_difference == 1 and pos2[0] == square_en_passant[0]:
        if (piece, square_en_passant[1], pos1[1], pos2[1]) == ('P', '5', '5', '6'):
            return True
        if (piece, square_en_passant[1], pos1[1], pos2[1]) == ('p', '4', '4', '3'):
            return True
    return False


if __name__ == "__main__":
    print(is_en_passant('P', 'a2', 'd4'))
