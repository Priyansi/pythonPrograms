import re


def pgn_to_moves():
    raw_PGN = ''.join(line.strip() for line in open('chessGame.pgn'))

    comments_replaced = raw_PGN.replace('{', '<').replace('}', '>')
    STRC = re.compile('<[^>]*>')
    comments_removed = STRC.sub('', comments_replaced)
    STRReplaced = comments_removed.replace('[', '<').replace(']', '>')
    STRRemoved = STRC.sub('', STRReplaced)
    NUMBERS = re.compile('[1-9][0-9]* *\.')
    moves_with_score = [_.strip() for _ in NUMBERS.split(
        STRRemoved) if len(_.strip()) > 0]
    last_move = moves_with_score[-1]
    SCORE = re.compile('( *1 *- *0| *0 *- *1| *1/2 *- *1/2)')
    last_move = SCORE.sub('', last_move)
    moves = moves_with_score[:-1]+[last_move]
    return moves


def pre_process_move(move):
    if ' ' not in move:
        if move[0] in 'abcdefgh':
            move = 'P'+move
        return move
    white_move, black_move = move.split()
    if white_move[0] in 'abcdefgh':
        white_move = 'P' + white_move
    if black_move[0] in 'abcdefgh':
        black_move = 'p' + black_move
    else:
        black_move = black_move.lower()
    return (white_move, black_move)


def pre_process_moves():
    moves = []
    for move in pgn_to_moves():
        combined_moves = pre_process_move(move)
        if len(combined_moves) == 2:
            moves.append(combined_moves[0])
            moves.append(combined_moves[1])
        else:
            moves.append(combined_moves)
    return moves


if __name__ == "__main__":
    print(pre_process_moves())
