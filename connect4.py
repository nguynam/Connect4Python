#!/usr/bin/env python

class Connect4:	
	row = 7
	col = 7
	win = 4
	board = [[0 for x in xrange(col)] for x in xrange(row)] 
	
	def __init__(self, row, col, win):
		self.row = row
		self.col = col
		self.win = win
	
