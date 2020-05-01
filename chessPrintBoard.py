NEWLINE = '\n'
SEPARATOR = '|'
BLANK_BOX = '_'+SEPARATOR


def formBoard(ranks):
    board = ''
    for rank in ranks:
        line = SEPARATOR
        for square in rank:
            line += int(square) * \
                BLANK_BOX if square.isdigit() else square+SEPARATOR
        board += line+NEWLINE
    return board


forsyth = 'r1bq1rk1/pp3ppp/3n4/2p1N3/2B5/7P/PPP2PP1/R1BQR1K1'
ranks = forsyth.split('/')
print(formBoard(ranks))
