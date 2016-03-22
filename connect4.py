#!/usr/bin/env python

import pickle

class Connect4:
	row_size = 7
	col_size = 7
	current_row = None
	current_col = None
	win = 4
	board = []
	winner = False

	def __init__(self, row, col, win):
		self.row_size = row
		self.col_size = col
		self.win = win
		self.board = [[0 for x in xrange(col)] for x in xrange(row)]

	def reset(self):
		self.board = [[0 for x in xrange(self.col_size)] for x in xrange(self.row_size)]

	def print_board(self):
		print
		for row in self.board:
			for e in row:
				print e,
			print

	def place_token(self, col, player):
		row = self.row_size - 1
		self.current_col = col
		while row >= 0:
			if self.board[row][col] == 0:
				self.board[row][col] = player
				self.current_row = row
				return 1
			else:
				row -= 1
		return 0

	def check_if_won(self):
		#Check Vertical Win
		count1 = 0
		count2 = 0
		for i in xrange(self.row_size - 1, -1, -1):
			if self.board[i][self.current_col] == 1:
				count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					print('Player 1 Won!')
					return 1

			elif self.board[i][self.current_col] == 2:
				count2 += 1
				count1 = 0
				if count2 == self.win:
					self.winner = True
					print('Player 2 Won!')
					return 2

		#Check Horizontal Win
		count1 = 0
		count2 = 0
		for i in xrange(self.col_size - 1, -1, -1):
			if self.board[self.current_row][i] == 1:
				count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					print('Player 1 Won!')
					return 1
			else:
				count1 = 0

			if self.board[self.current_row][i] == 2:
				count2 += 1
				count1 = 0
				if count2 == self.win:
					self.winner = True
					print('Player 2 Won!')
					return 2
			else:
				count2 = 0

		#Check Backward Diagonal
		count1 = 0
		count2 = 0
		curr_col = self.current_col
		curr_row = self.current_row

		while curr_col > 0 or curr_row < self.row_size - 1:
			if curr_row == self.row_size - 1 or curr_col == 0:
				break
			else:
				curr_col -= 1
				curr_row += 1

		while curr_col <= self.col_size - 1:
			if self.board[curr_row][curr_col] == 1:
				count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					return 1
			else:
				count1 = 0

			if self.board[curr_row][curr_col] == 2:
				count2 += 1
				count1 = 0
				if count2 == self.win:
					self.winner = True
					return 2
			else:
				count2 = 0

			curr_col += 1
			curr_row -= 1

		#Check Forward Diagonal
		count1 = 0
		count2 = 0
		curr_col = self.current_col
		curr_row = self.current_row

		while curr_col < self.col_size - 1 or curr_row < self.row_size - 1:
			if curr_row == self.row_size - 1 or curr_col == self.col_size - 1:
				break
			else:
				curr_col += 1
				curr_row += 1

		while curr_col >= 0:
			if self.board[curr_row][curr_col] == 1:
				count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					return 1
			else:
				count1 = 0

			if self.board[curr_row][curr_col] == 2:
				count2 += 1
				count1 = 0
				if count2 == self.win:
					self.winner = True
					return 2
			else:
				count2 = 0

			curr_col -= 1
			curr_row -= 1

	def save(self):
		output = open('myfile.pkl', 'wb')
		pickle.dump(self.board, output)
		output.close()

	def load(self):
		pkl_file = open('myfile.pkl', 'rb')
		self.board = pickle.load(pkl_file)
		pkl_file.close()

	def main(self):
		pass


current_player = 1
game = Connect4(7, 7, 4)

while game.winner == False:
	game.print_board()
	if current_player == 1:
		col = input('Player 1: ')
		game.place_token(col, current_player)
		game.check_if_won()
		current_player = 2
	elif current_player == 2:
		col = input("Player 2: ")
		game.place_token(col, current_player)
		game.check_if_won()
		current_player = 1

game.print_board()


