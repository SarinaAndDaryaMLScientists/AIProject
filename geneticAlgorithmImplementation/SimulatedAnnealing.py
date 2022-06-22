import chess

board = chess.Board()
# board.push_san("e4")
# board.san_and_push("e4")
turn = True
while True:
    mv = input("please enter your move: ")
    if chess.Move.from_uci(mv) in board.legal_moves:
        board.push_san(mv)
    turn = not turn
# print(board)
