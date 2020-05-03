import re
import chessPieceCanCapture
import chessCanMoveToPos
from collections import OrderedDict
NEWLINE = '\n'
END_OF_RANK = 'h'
SEPARATOR = '|'
EMPTY_SQUARE = '_'
CASTLING_QUEENS_SIDE = {'O': {'K': ('e1', 'c1'), 'R': ('a1', 'd1')}, 'o': {
    'k': ('e8', 'c8'), 'r': ('a8', 'd8')}}
CASTLING_KINGS_SIDE = {'O': {'K': ('e1', 'g1'), 'R': ('h1', 'f1')}, 'o': {
    'k': ('e8', 'g8'), 'r': ('h8', 'f8')}}
WHITE_VIEW_TEXT = '*'*16+NEWLINE+'  WHITE\'S MOVE'+NEWLINE+'*'*16
BLACK_VIEW_TEXT = '*'*16+NEWLINE+'  BLACK\'S MOVE'+NEWLINE+'*'*16


def setup():
    squares = [y+x for x in '12345678' for y in 'abcdefgh']
    start = 'RNBQKBNR'+'P'*8+EMPTY_SQUARE*8+EMPTY_SQUARE * \
        8+EMPTY_SQUARE*8+EMPTY_SQUARE*8+'p'*8+'rnbqkbnr'
    board_view = OrderedDict(zip(squares, start))
    piece_view = {_: [] for _ in 'BKNPQRbknpqr'}
    for square in squares:
        piece = board_view[square]
        if piece != EMPTY_SQUARE:
            piece_view[piece].append(square)
    return board_view, piece_view


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
    white_move, black_move = move.split()
    if white_move[0] in 'abcdefgh':
        white_move = 'P' + white_move
    if black_move[0] in 'abcdefgh':
        black_move = 'p' + black_move
    else:
        black_move = black_move.lower()
    return (white_move, black_move)


def pre_process_moves(moves):
    return [pre_process_move(move) for move in moves]


def remove_ambiguity(board_view, piece_view, piece, square_to_go, current_file_or_rank):
    for square_at in piece_view[piece]:
        if current_file_or_rank in square_at and chessCanMoveToPos.isMoveValid(piece, square_at, square_to_go):
            return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)


def update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go):
    board_view[square_to_go] = piece
    board_view[square_at] = EMPTY_SQUARE
    piece_view[piece].remove(square_at)
    piece_view[piece].append(square_to_go)
    return board_view, piece_view


def remove_capture_ambiguity(board_view, piece_view, piece, square_to_go, current_file_or_rank):
    for square_at in piece_view[piece]:
        if current_file_or_rank in square_at and chessPieceCanCapture.canPieceCapture(piece, square_at, square_to_go):
            piece_view = remove_captured_piece(
                board_view, piece_view, square_to_go)
            return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)


def remove_captured_piece(board_view, piece_view, square_to_go):
    piece_captured = board_view[square_to_go]
    piece_view[piece_captured].remove(square_to_go)
    return piece_view


def capture(board_view, piece_view, move):
    piece, square_to_go = move[0], move[-2:]
    if move != piece+square_to_go:
        return remove_capture_ambiguity(board_view, piece_view, piece, square_to_go, move.replace(piece, '').replace(square_to_go, ''))
    for square_at in piece_view[piece]:
        if chessPieceCanCapture.canPieceCapture(piece, square_at, square_to_go):
            piece_view = remove_captured_piece(
                board_view, piece_view, square_to_go)
            return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)


def movement(board_view, piece_view, move):
    piece, square_to_go = move[0], move[-2:]
    if move != piece+square_to_go:
        return remove_ambiguity(board_view, piece_view, piece, square_to_go, move.replace(piece, '').replace(square_to_go, ''))
    for square_at in piece_view[piece]:
        if chessCanMoveToPos.isMoveValid(piece, square_at, square_to_go):
            return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)


def castling_update_piece(board_view, piece_view, piece, castling_side, castling_player):
    return update_board_piece_view(
        board_view, piece_view, piece, castling_side[castling_player][piece][0], castling_side[castling_player][piece][1])


def castling(board_view, piece_view, move):
    castling_player = move[0]
    if castling_player == 'O':
        king, rook = 'K', 'R'
    else:
        king, rook = 'k', 'r'
    castling_side = CASTLING_KINGS_SIDE if move.lower() == 'o-o' else CASTLING_QUEENS_SIDE
    board_view, piece_view = castling_update_piece(
        board_view, piece_view, king, castling_side, castling_player)
    return castling_update_piece(board_view, piece_view, rook, castling_side, castling_player)


def status_after_each_turn(board_view, piece_view, move):
    if 'x' in move:
        return capture(board_view, piece_view, move.replace('x', ''))
    if 'o' in move.lower():
        return castling(board_view, piece_view, move)
    return movement(board_view, piece_view, move)


def print_white_board(board_view):
    board = ''
    files = ''
    for square in board_view:
        files += board_view[square]+SEPARATOR
        if END_OF_RANK in square:
            board += files[::-1]+SEPARATOR+NEWLINE
            files = ''
    return (board[::-1]).strip(NEWLINE)+NEWLINE


def print_black_board(board_view):
    board = ''
    for square in board_view:
        board += SEPARATOR+board_view[square]
        if END_OF_RANK in square:
            board += SEPARATOR+NEWLINE
    return board


def view(board_view, view_text):
    return print_white_board(board_view) + view_text if view_text == WHITE_VIEW_TEXT else print_black_board(board_view)+view_text


def game(moves):
    en_passant = ''
    board_view, piece_view = setup()
    all_moves = [view(board_view, WHITE_VIEW_TEXT)+NEWLINE +
                 view(board_view, BLACK_VIEW_TEXT)]
    for white_move, black_move in moves[:2]:
        currentBoard = 'CHECK'+NEWLINE if '+' in white_move else ''
        board_view, piece_view = status_after_each_turn(
            board_view, piece_view, white_move.strip('+'))
        currentBoard += view(board_view, WHITE_VIEW_TEXT)
        currentBoard += 'CHECK'+NEWLINE if '+' in black_move else ''
        board_view, piece_view = status_after_each_turn(
            board_view, piece_view, black_move.strip('+'))
        currentBoard += NEWLINE+view(board_view, BLACK_VIEW_TEXT)
        all_moves.append(currentBoard)
    return all_moves


print(game(pre_process_moves(pgn_to_moves()))[-1])
