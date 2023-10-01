import pygame

from Super_Piece import Super_Piece

#Pawn class
class Pawn(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		self.en_peasant = False
		super().__init__()

	#Identifies the valid moves for the piece
	def valid_moves(self, piece_x, piece_y, board, colour, prev_board):
		if colour == True:
			opp_colour = 'B'
			opp_pawn = 'B_Pawn'
		else:
			opp_colour = 'W'
			opp_pawn = 'W_Pawn'

		self.valid_moves_list = []

		if piece_y > 0:
			#Move forward one
			if board[piece_x][piece_y - 1][0] == False and piece_y > 0:
				self.valid_moves_list.append([piece_x, piece_y - 1])
				#Move forward 2 on first move
				if piece_y == 6 and board[piece_x][piece_y - 2][0] == False:
					self.valid_moves_list.append([piece_x, piece_y - 2])

		#Take top right
		if piece_x < 7:
			if board[piece_x + 1][piece_y - 1][0] != False and board[piece_x + 1][piece_y - 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x + 1, piece_y - 1])

		#Take top left
		if piece_x > 0:
			if board[piece_x - 1][piece_y - 1][0] != False and board[piece_x - 1][piece_y - 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x - 1, piece_y - 1])

		#En peasant
		if piece_y == 3:

			#Take right
			if piece_x < 7:
				if prev_board[piece_x + 1][piece_y - 2][0] == opp_pawn and board[piece_x + 1][piece_y][0] == opp_pawn and board[piece_x + 1][piece_y - 1][0] == False:
					self.valid_moves_list.append([piece_x + 1, piece_y - 1])
					self.en_peasant = True

			#Take left
			if piece_x > 0:
				if prev_board[piece_x - 1][piece_y - 2][0] == opp_pawn and board[piece_x - 1][piece_y][0] == opp_pawn and board[piece_x - 1][piece_y - 1][0] == False:
					self.valid_moves_list.append([piece_x - 1, piece_y - 1])
					self.en_peasant = True

	#Gets attacks for checks
	def get_attacks(self, piece_x, piece_y):
		attacks = []
		if piece_y > 0:
			if piece_x < 7:
				attacks.append([piece_x + 1, piece_y - 1])

			if piece_x > 0:
				attacks.append([piece_x - 1, piece_y - 1])

		return attacks

	def get_en_peasant(self):
		return self.en_peasant

	def set_en_peasant(self, boolean):
		self.en_peasant = boolean

#Knight class
class Knight(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		super().__init__()

	#Identifies the valid moves for the piece + take
	def valid_moves(self, piece_x, piece_y, board, colour):
		if colour == True:
			opp_colour = 'B'
		else:
			opp_colour = 'W'

		self.valid_moves_list = []

		#For long right up move
		if piece_x < 6 and piece_y > 0:
			if board[piece_x + 2][piece_y - 1][0] == False or board[piece_x + 2][piece_y - 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x + 2, piece_y - 1])

		#For short right up move + take
		if piece_x < 7 and piece_y > 1:
			if board[piece_x + 1][piece_y - 2][0] == False or board[piece_x + 1][piece_y - 2][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x + 1, piece_y - 2])

		#For long left up move
		if piece_x > 1 and piece_y > 0:
			if board[piece_x - 2][piece_y - 1][0] == False or board[piece_x - 2][piece_y - 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x - 2, piece_y - 1])

		#For short left up move + take
		if piece_x > 0 and piece_y > 1:
			if board[piece_x - 1][piece_y - 2][0] == False or board[piece_x - 1][piece_y - 2][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x - 1, piece_y - 2])

		#For long right down move
		if piece_x < 6 and piece_y < 7:
			if board[piece_x + 2][piece_y + 1][0] == False or board[piece_x + 2][piece_y + 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x + 2, piece_y + 1])

		#For short right down move + take
		if piece_x < 7 and piece_y < 6:
			if board[piece_x + 1][piece_y + 2][0] == False or board[piece_x + 1][piece_y + 2][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x + 1, piece_y + 2])

		#For long left down move
		if piece_x > 1 and piece_y < 7:
			if board[piece_x - 2][piece_y + 1][0] == False or board[piece_x - 2][piece_y + 1][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x - 2, piece_y + 1])

		#For short left down move + take
		if piece_x > 0 and piece_y < 6:
			if board[piece_x - 1][piece_y + 2][0] == False or board[piece_x - 1][piece_y + 2][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x - 1, piece_y + 2])

	#Gets all the knight's attacks
	def get_attacks(self, piece_x, piece_y):
		attacks = []

		#For long right up move
		if piece_x < 6 and piece_y > 0:
			attacks.append([piece_x + 2, piece_y - 1])

		#For short right up move + take
		if piece_x < 7 and piece_y > 1:
			attacks.append([piece_x + 1, piece_y - 2])

		#For long left up move
		if piece_x > 1 and piece_y > 0:
			attacks.append([piece_x - 2, piece_y - 1])

		#For short left up move + take
		if piece_x > 0 and piece_y > 1:
			attacks.append([piece_x - 1, piece_y - 2])

		#For long right down move
		if piece_x < 6 and piece_y < 7:
			attacks.append([piece_x + 2, piece_y + 1])

		#For short right down move + take
		if piece_x < 7 and piece_y < 6:
			attacks.append([piece_x + 1, piece_y + 2])

		#For long left down move
		if piece_x > 1 and piece_y < 7:
			attacks.append([piece_x - 2, piece_y + 1])

		#For short left down move + take
		if piece_x > 0 and piece_y < 6:
			attacks.append([piece_x - 1, piece_y + 2])

		#Returns attacks
		return attacks

#Bishop class
class Bishop(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		super().__init__()

	#Identifies the valid moves for the piece + take
	def valid_moves(self, piece_x, piece_y, board, colour):
		if colour == True:
			opp_colour = 'B'
		else:
			opp_colour = 'W'

		self.valid_moves_list = []

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y - 1
		running = True

		#Top right
		while pos_x < 8 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x += 1
				pos_y -= 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y - 1
		running = True

		#Top left
		while pos_x > -1 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x -= 1
				pos_y -= 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y + 1
		running = True

		#Bottom right
		while pos_x < 8 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x += 1
				pos_y += 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y + 1
		running = True

		#Bottom left
		while pos_x > -1 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x -= 1
				pos_y += 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

	#Gets attacks for bishop
	def get_attacks(self, board, piece_x, piece_y):

		attacks = []

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y - 1
		running = True

		#Top right
		while pos_x < 8 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x += 1
				pos_y -= 1
			else:
				attacks.append([pos_x, pos_y])
				running = False


		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y - 1
		running = True

		#Top left
		while pos_x > -1 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x -= 1
				pos_y -= 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y + 1
		running = True

		#Bottom right
		while pos_x < 8 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x += 1
				pos_y += 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y + 1
		running = True

		#Bottom left
		while pos_x > -1 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x -= 1
				pos_y += 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Returns bishop's attacks
		return attacks

#Rook class
class Rook(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		super().__init__()

	#Identifies the valid moves for the piece + take
	def valid_moves(self, piece_x, piece_y, board, colour):
		if colour == True:
			opp_colour = 'B'
		else:
			opp_colour = 'W'

		self.valid_moves_list = []

		#Sets coordinates to loop from + running condition
		pos_y = piece_y - 1
		running = True

		#Up
		while pos_y > -1 and running == True:
			if board[piece_x][pos_y][0] == False:
				self.valid_moves_list.append([piece_x, pos_y])
				pos_y -= 1
			elif board[piece_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_y = piece_y + 1
		running = True

		#Down
		while pos_y < 8 and running == True:
			if board[piece_x][pos_y][0] == False:
				self.valid_moves_list.append([piece_x, pos_y])
				pos_y += 1
			elif board[piece_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x + 1
		running = True

		#Right
		while pos_x < 8 and running == True:
			if board[pos_x][piece_y][0] == False:
				self.valid_moves_list.append([pos_x, piece_y])
				pos_x += 1
			elif board[pos_x][piece_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, piece_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x - 1
		running = True

		#Left
		while pos_x > -1 and running == True:
			if board[pos_x][piece_y][0] == False:
				self.valid_moves_list.append([pos_x, piece_y])
				pos_x -= 1
			elif board[pos_x][piece_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, piece_y])
				running = False
			else:
				running = False

	#Gets the rook's attack
	def get_attacks(self, board, piece_x, piece_y):

		attacks = []

		#Sets coordinates to loop from + running condition
		pos_y = piece_y - 1
		running = True

		#Up
		while pos_y > -1 and running == True:
			if board[piece_x][pos_y][0] == False:
				attacks.append([piece_x, pos_y])
				pos_y -= 1
			else:
				attacks.append([piece_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_y = piece_y + 1
		running = True

		#Down
		while pos_y < 8 and running == True:
			if board[piece_x][pos_y][0] == False:
				attacks.append([piece_x, pos_y])
				pos_y += 1
			else:
				attacks.append([piece_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x + 1
		running = True

		#Right
		while pos_x < 8 and running == True:
			if board[pos_x][piece_y][0] == False:
				attacks.append([pos_x, piece_y])
				pos_x += 1
			else:
				attacks.append([pos_x, piece_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x - 1
		running = True

		#Left
		while pos_x > -1 and running == True:
			if board[pos_x][piece_y][0] == False:
				attacks.append([pos_x, piece_y])
				pos_x -= 1
			else:
				attacks.append([pos_x, piece_y])
				running = False

		#Returns the rook's attacks
		return attacks

#There is 100% a better way of making these but I can't be bothered to think about it that much :)

#Queen class
class Queen(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		super().__init__()

	#Identifies the valid moves for the piece + take
	def valid_moves(self, piece_x, piece_y, board, colour):
		if colour == True:
			opp_colour = 'B'
		else:
			opp_colour = 'W'

		self.valid_moves_list = []

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y - 1
		running = True

		#Top right
		while pos_x < 8 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x += 1
				pos_y -= 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y - 1
		running = True

		#Top left
		while pos_x > -1 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x -= 1
				pos_y -= 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y + 1
		running = True

		#Bottom right
		while pos_x < 8 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x += 1
				pos_y += 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y + 1
		running = True

		#Bottom left
		while pos_x > -1 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				self.valid_moves_list.append([pos_x, pos_y])
				pos_x -= 1
				pos_y += 1
			elif board[pos_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_y = piece_y - 1
		running = True

		#Up
		while pos_y > -1 and running == True:
			if board[piece_x][pos_y][0] == False:
				self.valid_moves_list.append([piece_x, pos_y])
				pos_y -= 1
			elif board[piece_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_y = piece_y + 1
		running = True

		#Down
		while pos_y < 8 and running == True:
			if board[piece_x][pos_y][0] == False:
				self.valid_moves_list.append([piece_x, pos_y])
				pos_y += 1
			elif board[piece_x][pos_y][0][:1] == opp_colour:
				self.valid_moves_list.append([piece_x, pos_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x + 1
		running = True

		#Right
		while pos_x < 8 and running == True:
			if board[pos_x][piece_y][0] == False:
				self.valid_moves_list.append([pos_x, piece_y])
				pos_x += 1
			elif board[pos_x][piece_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, piece_y])
				running = False
			else:
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x - 1
		running = True

		#Left
		while pos_x > -1 and running == True:
			if board[pos_x][piece_y][0] == False:
				self.valid_moves_list.append([pos_x, piece_y])
				pos_x -= 1
			elif board[pos_x][piece_y][0][:1] == opp_colour:
				self.valid_moves_list.append([pos_x, piece_y])
				running = False
			else:
				running = False

	#Gets the queen's attacks
	def get_attacks(self, board, piece_x, piece_y):
		attacks = []

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y - 1
		running = True

		#Top right
		while pos_x < 8 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x += 1
				pos_y -= 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y - 1
		running = True

		#Top left
		while pos_x > -1 and pos_y > -1 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x -= 1
				pos_y -= 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x + 1, piece_y + 1
		running = True

		#Bottom right
		while pos_x < 8 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x += 1
				pos_y += 1
			else:
				attacks.append([pos_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x, pos_y = piece_x - 1, piece_y + 1
		running = True

		#Bottom left
		while pos_x > -1 and pos_y < 8 and running == True:
			if board[pos_x][pos_y][0] == False:
				attacks.append([pos_x, pos_y])
				pos_x -= 1
				pos_y += 1
			else:
				attacks.append([pos_x, pos_y])
				running = False
		#Sets coordinates to loop from + running condition
		pos_y = piece_y - 1
		running = True

		#Up
		while pos_y > -1 and running == True:
			if board[piece_x][pos_y][0] == False:
				attacks.append([piece_x, pos_y])
				pos_y -= 1
			else:
				attacks.append([piece_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_y = piece_y + 1
		running = True

		#Down
		while pos_y < 8 and running == True:
			if board[piece_x][pos_y][0] == False:
				attacks.append([piece_x, pos_y])
				pos_y += 1
			else:
				attacks.append([piece_x, pos_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x + 1
		running = True

		#Right
		while pos_x < 8 and running == True:
			if board[pos_x][piece_y][0] == False:
				attacks.append([pos_x, piece_y])
				pos_x += 1
			else:
				attacks.append([pos_x, piece_y])
				running = False

		#Sets coordinates to loop from + running condition
		pos_x = piece_x - 1
		running = True

		#Left
		while pos_x > -1 and running == True:
			if board[pos_x][piece_y][0] == False:
				attacks.append([pos_x, piece_y])
				pos_x -= 1
			else:
				attacks.append([pos_x, piece_y])
				running = False

		#Returns the queen's attacks
		return attacks


#King class
class King(Super_Piece):

	#Imports the single method in the parent class lol
	def __init__(self):
		super().__init__()

	#Identifies the valid moves for the piece + take
	def valid_moves(self, piece_x, piece_y, board, colour, castle_array):
		if colour == True:
			opp_colour = 'B'
			x = 2
		else:
			opp_colour = 'W'
			x = 1

		self.valid_moves_list = []

		#Setting up variable
		i = -1

		#Row above king
		if piece_y > 0:
			while i < 2:
				if not (piece_x == 0 and i == -1) and not (piece_x == 7 and i == 1) and (board[piece_x + i][piece_y - 1][x]) != True:
					if board[piece_x + i][piece_y - 1][0] == False:
						self.valid_moves_list.append([piece_x + i, piece_y - 1])
					elif board[piece_x + i][piece_y - 1][0][:1] == opp_colour:
						self.valid_moves_list.append([piece_x + i, piece_y - 1])
				i += 1

		#Tiles aside king
		if piece_x > 0:
			if (board[piece_x - 1][piece_y][x]) != True:
				if board[piece_x - 1][piece_y][0] == False:
					self.valid_moves_list.append([piece_x - 1, piece_y])
				elif board[piece_x - 1][piece_y][0][:1] == opp_colour:
					self.valid_moves_list.append([piece_x - 1, piece_y])

		if piece_x < 7:
			if (board[piece_x + 1][piece_y][x]) != True:
				if board[piece_x + 1][piece_y][0] == False:
					self.valid_moves_list.append([piece_x + 1, piece_y])
				elif board[piece_x + 1][piece_y][0][:1] == opp_colour:
					self.valid_moves_list.append([piece_x + 1, piece_y])

		#Setting up variable
		i = -1

		#Row below king
		if piece_y < 7:
			while i < 2:
				if not (piece_x == 0 and i == -1) and not (piece_x == 7 and i == 1) and (board[piece_x + i][piece_y + 1][x]) != True:
					if board[piece_x + i][piece_y + 1][0] == False:
						self.valid_moves_list.append([piece_x + i, piece_y + 1])
					elif board[piece_x + i][piece_y + 1][0][:1] == opp_colour:
						self.valid_moves_list.append([piece_x + i, piece_y + 1])
				i += 1

		#Castling
		if colour == True and castle_array[0] == False or colour == False and castle_array[1] == False:

			#Left castling for white
			if castle_array[3] == False and colour == True and board[0][7][0] == 'W_Rook':
				if board[piece_x][piece_y][x] == False and board[piece_x - 1][piece_y][x] == False and board[piece_x - 2][piece_y][x] == False and board[piece_x - 1][piece_y][0] == False and board[piece_x - 2][piece_y][0] == False and board[piece_x - 3][piece_y][0] == False:
					self.valid_moves_list.append([piece_x - 2, piece_y])

			#Right castling for black
			if castle_array[5] == False and colour == False and board[7][7][0] == 'B_Rook':
				if board[piece_x][piece_y][x] == False and board[piece_x + 1][piece_y][x] == False and board[piece_x + 2][piece_y][x] == False and board[piece_x + 1][piece_y][0] == False and board[piece_x + 2][piece_y][0] == False and board[piece_x + 3][piece_y][0] == False:
					self.valid_moves_list.append([piece_x + 2, piece_y])

			#Right castling for white
			if castle_array[3] == False and colour == True and board[7][7][0] == 'W_Rook':
				if board[piece_x][piece_y][x] == False and board[piece_x + 1][piece_y][x] == False and board[piece_x + 2][piece_y][x] == False and board[piece_x + 1][piece_y][0] == False and board[piece_x + 2][piece_y][0] == False:
					self.valid_moves_list.append([piece_x + 2, piece_y])

			#Left castling for black
			if castle_array[4] == False and colour == False and board[0][7][0] == 'B_Rook':
				if board[piece_x][piece_y][x] == False and board[piece_x - 1][piece_y][x] == False and board[piece_x - 2][piece_y][x] == False and board[piece_x - 1][piece_y][0] == False and board[piece_x - 2][piece_y][0] == False:
					self.valid_moves_list.append([piece_x - 2, piece_y])

	#Gets all the squares the king attacks
	def get_attacks(self, piece_x, piece_y):

		#Setting up variables
		attacks = []
		i = -1

		#Row above king
		if piece_y > 0:
			while i < 2:
				if not (piece_x == 0 and i == -1) and not (piece_x == 7 and i == 1):
					attacks.append([piece_x + i, piece_y - 1])
					attacks.append([piece_x + i, piece_y - 1])
				i += 1

		#Tiles aside king
		if piece_x > 0:
			attacks.append([piece_x - 1, piece_y])
			attacks.append([piece_x - 1, piece_y])

		if piece_x < 7:
			attacks.append([piece_x + 1, piece_y])
			attacks.append([piece_x + 1, piece_y])

		#Setting up variable
		i = -1

		#Row below king
		if piece_y < 7:
			while i < 2:
				if not (piece_x == 0 and i == -1) and not (piece_x == 7 and i == 1):
					attacks.append([piece_x + i, piece_y + 1])
					attacks.append([piece_x + i, piece_y + 1])
				i += 1

		#Returns attacks
		return attacks