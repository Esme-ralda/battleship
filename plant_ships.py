from board import *
from random import randint
from copy import deepcopy

def define_pos():
	a = randint(0,1)
	if a == 0:
		return "vertical"
	elif a==1:
		return "horizontal"

def plant_shippe(num,occupied,board):
	'''Find a point on board to start a ship so that the ship does not go off board
	build a ship downwards if vertical to the left if horizontal
	check if each segment is absent from the occupied list
	if occupied, start again'''
	bound = randint(0,len(board) - num-1)
	unbound = randint(0,len(board)-1)
	pos = define_pos()
	if pos == "vertical":
		ship = [(unbound, bound)]
		for point in range(num):
			ship.append((unbound, bound + point))
		for segment in ship:
			if segment in occupied:
				return plant_shippe(num,occupied,board)
		return ship
	elif pos == "horizontal":
		ship = [(bound, unbound)]
		for point in range(num):
			ship.append((bound+point, unbound))
		for segment in ship:
			if segment in occupied:
				return plant_shippe(num,occupied,board)
		return ship

def find_neighbors(board, point):
	x = point[0]
	y = point[1]
	neighbors = []
	neighbors.append((x+1,y))
	neighbors.append((x-1,y))	
	neighbors.append((x,y+1))
	neighbors.append((x,y-1))
	for neighbor in neighbors:
		if neighbor[0] > len(board)-1 or neighbor[0] < 0:
#			print neighbor
			neighbors.remove(neighbor)
		elif neighbor[1] > len(board)-1 or neighbor[1] < 0:
#			print neighbor
			neighbors.remove(neighbor)
	return neighbors


def calculate_occupied(ship, board):
	'''calculate fields on board occupied by ship and their neighbors
	return a set (?) of occupied'''
	occupied = deepcopy(ship)
	for point in ship:
		patmat = find_neighbors(board, point)
		for guy in patmat:
			if guy not in occupied:
				occupied.append(guy)
	return occupied

def deploy_ships(shiplist,board, names):
	occupied = set()
	ships_dict = dict()
	for index in range(len(shiplist)):
		s = plant_shippe(shiplist[index],occupied, board)
		for field in calculate_occupied(s, board):
			occupied.add(field)
		for point in s:
			ships_dict[point] =names[index]
	return ships_dict,occupied

#TODO remove occupied from deploy_ship returns
#TODO list index put of range przy wartosci 12 (skad ona?!)

if __name__ == '__main__':	
	ships = [4,3,3,2,2,2,1,1,1,1]
#	ships=[4]
	names = ['Battleship Potemkin','Red October','Black Pearl', \
	'Bounty','Arabella','Demeter','Flying Dutchman', 'Das Boot','Yellow Submarine',\
	'Nautilus']
	#~ board = make_board(12)

	#~ d,o = deploy_ships(ships, board, names)
	#~ preview = board_preview(board, o,d.keys())
	#~ print_board(board)
	#~ for key,value in d.iteritems():
		#~ if value=="Battleship Potemkin":
			#~ print value, key
	#~ print len(d.keys())
	
	counter = 0
	while counter <20:
		board = make_board(12)
		d,o = deploy_ships(ships, board, names)
		for point in o:
			x,y = point
			if x==12 or y==12:
				print d.keys()
				print o
		counter +=1
	else:
		print "No mistakes!"