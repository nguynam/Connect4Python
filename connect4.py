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
	
	def __placetoken__(self, col):
		return 0
		
	def __winner__(self):
		return 0
x = Connect4(6, 6, 4)
x.printboard(x.board)	
