#functios to handle board in Battleship Potemkin

def make_board(n):
	board = []
	for i in range(n):
		board.append(["O"]*n)
	return board

def print_board(board):
	for row in board:
		for point in row:
			print point,
		print '\n',

def board_preview(board, occupied, ships):
	#for marking deployed ships
	for a in occupied:
		x,y=a
		board[y][x]="x"
	for s in ships:
		x,y=s
		board[y][x]="#"

if __name__ == '__main__':
	board = make_board(12)
	print_board(board)
