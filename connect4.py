#!/usr/bin/env python

class Connect4:
	row = 7
	col = 7
	win = 4
	board = []
	winner = False

	def __init__(self, row, col, win):
		self.row = row
		self.col = col
		self.win = win
		self.board = [[0 for x in xrange(col)] for x in xrange(row)]


	def print_board(self, board):
		for row in board:
			for e in row:
				print e,
			print


	def place_token(self, col):
		i = self.row - 1
		while i >= 0:
			if self.board[i][col] == 0:
				self.board[i][col] = 1
				return 1
			else:
				i -= 1
		return 0


	def winner(self):
		pass


	def main(self):
		pass


game = Connect4(7, 7 ,4)
game.place_token(6)
game.place_token(6)
game.place_token(6)
game.place_token(6)
game.place_token(6)
game.place_token(6)
game.place_token(6)
game.print_board(game.board)
