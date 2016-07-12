import sys ### For printing inline
from math import sqrt

class Sudoku:
	"""This class is capable of solving a given sudoku in a lists of a list format."""

	def __init__(self, game = None, size = 9):
		"""Class constructor."""
		self.size = size
		self.box = int(sqrt(size))
		self.game = game

	def solve(self):
		"""Try to solve the game using backtrack."""
		if self.backtrack() == True:
			return True
		print "Impossible to solve"
		return False

	def backtrack(self):
		"""Backtracking."""
		succeeded, row, col = self.findEmpty()
		if not succeeded:
			return True
		for i in range(1, self.size + 1): # check all candidates
			if self.checkCandidate(i, row, col) == True:
				self.game[row][col] = i
				if self.backtrack() == True:
					return True
				self.game[row][col] = 0 # backtracking
		return False

	def findEmpty(self):
		"""Find empty cell in grid."""
		for i in range(0, self.size):
			for k in range(0, self.size):
				if self.game[i][k] == 0:
					return True, i, k
		return False, -1, -1

	def checkCandidate(self, i, row, col):
		"""Check if i number can be in the grid at row and col."""
		for k in range(0, self.size):
			if self.game[row][k] == i:
				return False
			if self.game[k][col] == i:
				return False
		for k in range(row/self.box * self.box, row/self.box * self.box + self.box):
			for j in range(col/self.box * self.box, col/self.box*self.box + self.box):
				if self.game[k][j] == i:
					return False
		return True

	def printOutput(self):
		"""Print result matrix."""
		for i in range(0, self.size):
			for k in range(0, self.size):
				sys.stdout.write(str(self.game[i][k])+ " ")
			sys.stdout.write("\n")

### DEBUG: ###
# Very hard example for test
game = [[0,9,0,0,0,0,3,0,0],
		[0,0,0,0,3,0,0,0,1],
		[0,0,0,0,0,0,0,6,0],
		[9,0,4,0,0,0,8,0,0],
		[7,0,0,6,0,9,0,0,3],
		[0,0,2,0,0,0,0,0,5],
		[0,0,0,0,0,0,0,0,0],
		[6,0,0,0,0,0,0,0,0],
		[0,0,0,1,0,0,0,3,0]]

if __name__ == "__main__":
	game = Sudoku(game)
	game.solve()
	game.printOutput()