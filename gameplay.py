import string
from plant_ships import *

#~ col = raw_input('Guess column:')
#~ row = raw_input('Guess row:')
#~ col = string.uppercase.index['col']
#~ print col,row


if __name__ == '__main__':	
	ships = [4,3,3,2,2,2,1,1,1,1]
	names = ['Battleship Potemkin','Red October','Black Pearl', \
	'Bounty','Arabella','Demeter','Flying Dutchman', 'Das Boot','Yellow Submarine',\
	'Nautilus']
	board = make_board(10)
	#print make_board.__doc__
	
	d,o = deploy_ships(ships, board)
	occupied = []
	
#	board_preview(board,o,d)
#	board = make_board(10)
	
	print_board(board)
	#ask for column and row, transform a letter into x value
	col = raw_input('Guess column:')
	row = int(raw_input('Guess row:'))
	col = int(string.uppercase.index(col))

	if col not in range(0, len(board[0])) or row not in range(0,len(board[0])):
		print 'Oops, that\'s not in the ocean'
	elif (row,col) in occupied:
		print 'Too close to the sunken ship'
		# turn counter not increased
	elif board[row][col] == 'X':
		print 'You have already guessed that field.'
	elif (col,row) not in d:
		print "You missed!"
	elif (col,row) in d:
		board[row][col]='X'
		ship_index = d[(col,row)]
		print ship_index
		ships[ship_index] = ships[ship_index] -1
		print ships
		print d
		if ships[ship_index] == 0:
			print 'You\'ve sunken',names[ship_index]+'!'
			#add occupied
		else:
			print "You hit a ship!"
	'''evaluate turn:
	print board
	ask col/row
	1. not in the ocean
	2. close proximity of a sunken ship (occupied)
	3. already guessed
	4. missed
	5. hit
	6. sinking + increment occupied'''

