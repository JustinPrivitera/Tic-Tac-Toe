#!/usr/bin/python3

import sys

BOARD_LENGTH = 3

def play_test():
	board = [[1, 0, 1], [-1, 1, 0], [1, -1, -1]] # 1 = X, -1 = O, 0 = blank
	print(str_board(board), end = '')
	print(check_win(board))

def play():
	board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
	# need a method to print the board and print over the previous board depending on what move is made

	xs = True
	while(check_win(board) == -1):
		print(str_board(board), end = '')
		move = int(input()) # need a way to check it is valid - 1) that it is an int between 1 and 9, and 2) that the place is not taken
		row = 0
		if move < 4:
			row = 0
		elif move < 7:
			row = 1
			move -= 3
		else:
			row = 2
			move -= 6
		if xs == True:
			board[row][move - 1] = 1
			xs = False
		else:
			board[row][move - 1] = -1
			xs = True

	# display results, start new game
	print(str_board(board), end = '')
	
def check_win(board): # return 0 if O's win, 1 if X's win, and -1 if it is incomplete and 2 if it is a draw
# abstract this method into more smaller methods
	sum_diag = 0
	sum_col = 0
	i = 0
	while i < BOARD_LENGTH:
		if sum(board[i]) == BOARD_LENGTH:
			print("flag 1")
			return 1
		elif sum(board[i]) == -BOARD_LENGTH:
			print("flag 2")
			return 0
		
		j = 0
		while j < BOARD_LENGTH:
			sum_col += board[j][i]
			j += 1
		if sum_col == BOARD_LENGTH:
			print("flag 3")
			return 1
		elif sum_col == -BOARD_LENGTH:
			print("flag 4")
			return 0
		
		sum_diag += board[i][i]
		i += 1
	
	if sum_diag == BOARD_LENGTH:
		print("flag 5")
		return 1
	elif sum_diag == -BOARD_LENGTH:
		print("flag 6")
		return 0
	sum_diag = board[0][2] + board[1][1] + board[2][0]
	if sum_diag == BOARD_LENGTH:
		print("flag 7")
		return 1
	elif sum_diag == -BOARD_LENGTH:
		print("flag 8")
		return 0

	if check_draw(board) == 1:
		print("flag 9")
		return 2

	return -1

def check_draw(board): # returns 1 if there is a draw and 0 if not
	num_zeros = 0
	i = 0
	while i < BOARD_LENGTH:
		j = 0
		while j < BOARD_LENGTH:
			if board[i][j] == 0:
				num_zeros += 1
			j += 1
		i += 1

	if num_zeros == 0:
		return 1
	return 0
		

def print_board(board):
	i = 0
	while i < BOARD_LENGTH:
		j = 0
		while j < BOARD_LENGTH:
			if board[i][j] == 0:
				print("   ", end = '')
			elif board[i][j] == -1:
				print(" O ", end = '')
			elif board[i][j] == 1:
				print(" X ", end = '')
			else:
				print("error")
				# exit status with information
			j += 1
		print()
		i += 1

def str_board(board):
	s_board = ""
	i = 0
	while i < BOARD_LENGTH:
		j = 0
		while j < BOARD_LENGTH:
			if board[i][j] == 0:
				s_board += "   "
			elif board[i][j] == -1:
				s_board += " O "
			elif board[i][j] == 1:
				s_board += " X "
			else:
				sys.stderr.write("error\n")
				# exit status with information
			j += 1
		s_board += "\n"
		i += 1
	return s_board

#play_test()

play()
