# strings = ["a", "e", "i", "o", "u"]
# result = ''
# for s in strings:
# 	result += s +","
# print("строка:" result)
#
# vowols = ["a", "e", "i", "o", "u"]
# vowols_str = ",".jon(vowols)
# print("Строка", vowols_str)

box = "*"
# board = []
# for i in range(8):
# row = [EMPTY for i in range(8)]
#
board = [[box for i in range(8)] for j in range(8)]
board[0][0] = "R"
board[0][1] = "N"
board[0][2] = "B"
board[0][3] = "Q"
board[0][4] = "K"
board[0][5] = "B"
board[0][6] = "N"
board[0][7] = "R"

for i in range(len(board)):
	# board[ 0 ][ 0 ] = ROOK
	print("\t".join(board[i]))
