#functios to handle board in Battleship Potemkin
import string

def make_board(n):
	board = []
	for i in range(n):
		board.append(["O"]*n)
	return board

def print_board(board):
	head = string.ascii_uppercase[0:len(board[0])]
	print '    ',
	for letter in head:
		print letter,
	print '\n'
	c = 0
	for row in board:
		print string.digits[c] , '  ',
		for point in row:
			print point,
		print '\n',
		c+=1

def board_preview(board, occupied, ships):
	#for marking deployed ships
	for a in occupied:
		x,y=a
		board[y][x]="x"
	for s in ships:
		x,y=s
		board[y][x]="#"
	print_board(board)

if __name__ == '__main__':
	board = make_board(12)
	print_board(board)
