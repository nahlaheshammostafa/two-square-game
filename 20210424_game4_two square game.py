import random

def printboard():
	print()
	for i,x in enumerate(game):
		print(x, end="\t")
		if ((i+1) % size == 0):
			print()


def getvalidmove(turn):
	data = input('Player '+ turn +', Enter your next move "x,y": ')
	while True:
			x,y = data.split(',')
			x = int(x)
			y = int(y)
			if (x > y):
				x,y = y,x

			if ((x > 0 and y > 0) and (x <= size2 and y <= size2) and ((y-x == size) or (y-x == 1 and x % size != 0))):
				if (game[x-1]=='X' or game[y-1]=='X'):
					data = input('The square is covered, please re-enter: ')
				else:
					return x,y
			else:
				data = input('Unallowed move, please re-enter: ')

def Possiblity():
	for i in range(size2):
		if ((i+1) % size != 0 and (i+1)<size2 and game[i] != 'X' and game[i+1] != 'X'):
			return True
		elif ((i + size) < size2 and game[i] != 'X' and game[i+size] != 'X'):
			return True
	return False





def squaregame():
	print('--------------------------------------')
	global game
	game = list(range(1,size2+1))

	turn = "0"
	x = 0
	y = 0
	while (Possiblity()):
		printboard()
		if turn == "1":
			turn = "2"
		else:
			turn = "1"

		x, y = getvalidmove(turn)

		game[x-1]='X'
		game[y-1]='X'
	printboard()

	print('Player',turn,"is the winner!")
def main():
	squaregame()

size = 4
size2 = size*size

game = []

main()