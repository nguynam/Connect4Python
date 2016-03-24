#!/usr/bin/env python

import pickle
import sys

class Connect4:
	row_size = 7
	col_size = 7
	current_row = None
	current_col = None
	win = 4
	board = []
	winner = False

	def reset(self):
		self.board = [[0 for x in xrange(self.col_size)] for x in xrange(self.row_size)]

	def print_board(self):
		for i in xrange(1, self.col_size + 1):
			print i,
		print

		for i in xrange(1, self.col_size + 1):
			print('-'),
		print

		for row in self.board:
			for e in row:
				print e,
			print

	def place_token(self, col, player):
		row = self.row_size - 1
		self.current_col = col - 1
		while row >= 0:
			if self.board[row][col - 1] == 0:
				self.board[row][col - 1] = player
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
				increment = lambda x: count1 + x
				count1 = increment(1)
				# count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					print('Player 1 Won!')
					return 1

			elif self.board[i][self.current_col] == 2:
				increment = lambda x: count2 + x
				count2 = increment(1)
				#count2 += 1
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
				increment = lambda x: count1 + x
				count1 = increment(1)
				#count1 += 1
				count2 = 0
				if count1 == self.win:
					self.winner = True
					print('Player 1 Won!')
					return 1
			else:
				count1 = 0

			if self.board[self.current_row][i] == 2:
				increment = lambda x: count2 + x
				count2 = increment(1)
				#count2 += 1
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

		while curr_col <= self.col_size - 1 and curr_row >= 0:
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

		while curr_col >= 0 and curr_row >= 0:
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
		current_player = 1
		self.col_size = int(sys.argv[1])
		self.row_size = int(sys.argv[2])
		self.win = int(sys.argv[3])
		self.reset()
		while game.winner == False:
			game.print_board()
			player1_won = False
			player2_won = False
			try:
				if current_player == 1:
					col = raw_input('Player 1: ')
					if col == 'save':
						game.save()
					elif col == 'load':
						game.load()
					elif col == 'reset':
						game.reset()
					else:
						col = int(col)
						if game.place_token(col, current_player) == 1:
							player1_won = True
						game.check_if_won()
						current_player = 2

				elif current_player == 2:
					col = raw_input("Player 2: ")
					if col == 'save':
						game.save()
					elif col == 'load':
						game.load()
					elif col == 'reset':
						game.reset()
					else:
						col = int(col)
						if game.place_token(col, current_player) == 2:
							player2_won = True
						game.check_if_won()
						current_player = 1

			except:
				print("Invalid Input")

		game.print_board()
		if(player1_won):
			print('Player 1 Won!')
		else:
			print('Player 2 Won!')

if __name__ == "__main__":
	game = Connect4()
	game.main()
