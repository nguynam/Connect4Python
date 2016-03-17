#!/usr/bin/env python

class Connect4:	
	row = 7
	col = 7
	win = 4
	board = []
	
	def __init__(self, row, col, win):
		self.row = row
		self.col = col
		self.win = win
		self.board = [[0 for x in xrange(col)] for x in xrange(row)]
		
	def printboard(self, board):
		for row in board:
			for e in row:
			    print e,
			print 
	
	def placetoken(self, col):
		i = self.row - 1
		while(i > 0):
			if (self.board[i][col] == 0):
				self.board[i][col] = 1
				break
			else:
				i = i - 1
		
	def winner(self):
		return 0
x = Connect4(6, 6, 4)
x.placetoken(2)
x.printboard(x.board)