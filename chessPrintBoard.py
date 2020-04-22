PIECES = {'K': '♔', 'Q': 1, 'R': 2, 'B': 3, 'N': 4, 'P': 5,
          'k': 6, 'q': 7, 'r': 8, 'b': 9, 'n': 10, 'p': 11}

UNICODE_CHESS = 9812
NEWLINE = '\n'
BLANK_BOX = '_'


def formBoard(positions):
    board = ''
    for row in positions:
        line = ''
        for column in row:
            line += int(column)*BLANK_BOX if column.isdigit() else column
        board += line+NEWLINE
    return board


positions = 'r3r1k1/pp3nPp/1b1p1B2/1q1P1N2/8/P4/Q2/1P3PK1/R6R'.split('/')
print(formBoard(positions))
