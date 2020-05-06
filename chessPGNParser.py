import chessPGNToMoves
import chessPieceCanCapture
import chessCanMoveToPos
import chessEnPassant
from collections import OrderedDict
NEWLINE, END_OF_RANK, SEPARATOR, EMPTY_SQUARE, EN_PASSANT, CHECK = '\n', 'h', '|', '_', 'ep', '+'
CASTLING_QUEENS_SIDE = {'O': {'K': ('e1', 'c1'), 'R': ('a1', 'd1')}, 'o': {
    'k': ('e8', 'c8'), 'r': ('a8', 'd8')}}
CASTLING_KINGS_SIDE = {'O': {'K': ('e1', 'g1'), 'R': ('h1', 'f1')}, 'o': {
    'k': ('e8', 'g8'), 'r': ('h8', 'f8')}}
WHITE_MOVE_TEXT = '*'*16+NEWLINE+'  WHITE\'S MOVE'+NEWLINE+'*'*16
BLACK_MOVE_TEXT = '*'*16+NEWLINE+'  BLACK\'S MOVE'+NEWLINE+'*'*16
WHITE_PIECES = 'BKNPQR'
BLACK_PIECES = 'bknpqr'


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
    piece_view[EN_PASSANT] = ''
    return board_view, piece_view


def is_rook_jumping_pieces(board_view, square_at, square_to_go):
    rank_difference = int(square_at[1])-int(square_to_go[1])
    if rank_difference == 0:
        files_arr = [chr(i)
                     for i in range(ord(square_at[0]), ord(square_to_go[0]))]
        for i in files_arr[1:]:
            if board_view[i+square_at[1]] != '_':
                return True
    else:
        step = 1 if rank_difference > 0 else -1
        for i in range(int(square_at[1])+1, int(square_to_go[1]), step):
            if board_view[square_at[0]+str(i)] != '_':
                return True
    return False


def remove_movement_ambiguity(board_view, piece_view, piece, square_to_go, current_file_or_rank):
    for square_at in piece_view[piece]:
        if piece.lower() == 'p':
            if current_file_or_rank in square_at and chessEnPassant.is_en_passant(piece, square_at, square_to_go):
                piece_view[EN_PASSANT] = square_to_go
                return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)
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
        if piece_view[EN_PASSANT] != '' and piece.lower() == 'p':
            if current_file_or_rank in square_at and chessEnPassant.can_capture_en_passant(piece, piece_view[EN_PASSANT], square_at, square_to_go):
                piece_view = remove_captured_piece(
                    board_view, piece_view, piece_view[EN_PASSANT])
                board_view[piece_view[EN_PASSANT]] = EMPTY_SQUARE
                piece_view[EN_PASSANT] = ''
                return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)
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
        if piece_view[EN_PASSANT] != '' and piece.lower() == 'p':
            if chessEnPassant.can_capture_en_passant(piece, piece_view[EN_PASSANT], square_at, square_to_go):
                piece_view = remove_captured_piece(
                    board_view, piece_view, piece_view[EN_PASSANT])
                board_view[piece_view[EN_PASSANT]] = EMPTY_SQUARE
                piece_view[EN_PASSANT] = ''
                return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)
        if chessPieceCanCapture.canPieceCapture(piece, square_at, square_to_go):
            if piece.lower() == 'r' and is_rook_jumping_pieces(board_view, square_at, square_to_go):
                continue
            piece_view = remove_captured_piece(
                board_view, piece_view, square_to_go)
            return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)


def movement(board_view, piece_view, move):
    piece, square_to_go = move[0], move[-2:]
    if move != piece+square_to_go:
        return remove_movement_ambiguity(board_view, piece_view, piece, square_to_go, move.replace(piece, '').replace(square_to_go, ''))
    for square_at in piece_view[piece]:
        if piece.lower() == 'p':
            if chessEnPassant.is_en_passant(piece, square_at, square_to_go):
                piece_view[EN_PASSANT] = square_to_go
                return update_board_piece_view(board_view, piece_view, piece, square_at, square_to_go)
        if chessCanMoveToPos.isMoveValid(piece, square_at, square_to_go):
            if piece.lower() == 'r' and is_rook_jumping_pieces(board_view, square_at, square_to_go):
                continue
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


def print_board(board_view):
    board = ''
    files = ''
    for square in board_view:
        files += board_view[square]+SEPARATOR
        if END_OF_RANK in square:
            board += files[::-1]+SEPARATOR+NEWLINE
            files = ''
    return (board[::-1]).strip(NEWLINE)+NEWLINE


def game(moves):
    board_view, piece_view = setup()
    all_moves = []
    for move in moves:
        currentBoard = 'CHECK'+NEWLINE if CHECK in move else ''
        board_view, piece_view = status_after_each_turn(
            board_view, piece_view, move.strip(CHECK))
        move_text = WHITE_MOVE_TEXT if move[0] in WHITE_PIECES else BLACK_MOVE_TEXT
        currentBoard += print_board(board_view)+move_text
        all_moves.append(currentBoard)
    return all_moves


print(game(chessPGNToMoves.pre_process_moves())[-1])
