# neural chess

import chess
board = chess.Board()

moves = []

readfile = open("moves-temp.txt", "r")

for line in readfile:
    Type = line.split(" ")
   
for i in range(0, len(Type)):
	a, b = Type[i].split(".")
	# a, b = b.split("/")
	moves.append(b)

i = 0
for move in moves:
	i += 1
	print("\nmove number: ",i)
	board.push_san(move)
	print(board)

print("stalemate: ",board.is_stalemate())

print("insufficient_material: ",board.is_insufficient_material())

print("gameover: ",board.is_game_over())

print(board.legal_moves)
# print(board)
# print(board.legal_moves)

# board.push_san("e4")
# board.push_san("e5")
# board.push_san("Qf3")
# print(board)
# print(board.legal_moves)
# print(board.is_checkmate())
