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

	d,o = deploy_ships(ships, board)
	print_board(board)
	#ask for column and row, transform a letter into x value
	col = raw_input('Guess column:')
	row = raw_input('Guess row:')
	col = string.uppercase.index(col)

	'''evaluate turn:
	1. not in the ocean
	2. close proximity of a sunken ship (occupied)
	3. already guessed
	4. missed
	5. hit
	6. sinking + increment occupied'''

