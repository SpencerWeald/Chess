#Important imports
import pygame, os, time

#Imports important classes
from Pieces import Pawn
from Pieces import Knight
from Pieces import Bishop
from Pieces import Rook
from Pieces import Queen
from Pieces import King

#Creates the board
class Board():

	#Initialises properties
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont("Comic Sans", 65)

		self.green_surface_square = pygame.Surface([90,90])
		self.green_surface_square.fill((170, 233, 170))
		self.cream_surface_square = pygame.Surface([90,90])
		self.cream_surface_square.fill((255, 252, 201))

		#Initialise piece class
		self.pawn = Pawn()
		self.knight = Knight()
		self.bishop = Bishop()
		self.rook = Rook()
		self.queen = Queen()
		self.king = King()

		#Image things
		self.images = {}
		#Goes to 'Pieces' folder
		imagesDirectory = 'Pieces'
		for fileName in os.listdir(imagesDirectory):
			if not fileName.endswith('.png'):
				continue
			#Loads all .png files
			image = pygame.image.load('Pieces' + r'/' + fileName)
			#Scales images
			image = pygame.transform.scale(image, (90, 90))
			#The file name is stored as the 0 index
			self.images[fileName.split('.')[0]] = image

		self.selected_piece = ''

	#Creates board
	def create_board(self):
		self.create_board = [[['B_Rook',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Rook',False,False]],[['B_Knight',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Knight',False,False]],[['B_Bishop',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Bishop',False,False]],[['B_Queen',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Queen',False,False]],[['B_King',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_King',False,False]],[['B_Bishop',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Bishop',False,False]],[['B_Knight',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Knight',False,False]],[['B_Rook',False,False],['B_Pawn',False,False],[False,False,False],[False,False,False],[False,False,False],[False,False,False],['W_Pawn',False,False],['W_Rook',False,False]]]

	#Returns the board
	def get_board(self):
		return self.create_board

	#Flips pieces
	def flip_board(self, board):
		new = []
		for file in range(8):
			temp = []
			for rank in range(8):
				temp.append(board[7-file][7-rank])
			new.append(temp)
		#board = new
		return new.copy()

	#Draws board, borw (black or white) determines which board to draw, 0 == white, 1 == black
	def draw_board(self, borw, promotion):

		#Sets up variables
		x = 0
		y = 0
		px, py = 0, 0
		pointer = 0

		#This gets the correct board pattern for white
		while y != 9:
			if y != 8 and x != 0:
				if (x + y) % 2 == 1:
					self.screen.blit(self.cream_surface_square,(px, py))
				else:
					self.screen.blit(self.green_surface_square,(px, py))
			#Draws positions
			elif promotion == False:
				if borw == True:
					text = ['8','7','6','5','4','3','2','1','','A','B','C','D','E','F','G','H','']
				elif borw == False:
					text = ['1','2','3','4','5','6','7','8','','H','G','F','E','D','C','B','A','']
				pos = self.font.render(text[pointer], True, (0, 0, 0))
				self.screen.blit(pos, (px + 22.5, py))
				if pointer != len(text) - 1:
					pointer += 1

			#Increments
			x += 1
			px += 90
			if x == 9:
				px = 0
				py += 90
				y += 1
				x = 0

	#Draws pieces
	def draw_piece(self, board):
		for i in range(8):
			for j in range(8):
				if board[i][j][0] != False:
					self.screen.blit(self.images[board[i][j][0]],(i*90 + 87, j*90))

	#Gets the checks of the opposite colour, this is really inefficient but I'm not gonna stress about it :)
	def get_all_relevant_checks(self, board, colour):

		if colour == True:
			x = 1
			y = 2
		else:
			x = 2
			y = 1

		#Checks array
		checks = []

		#Loops through the board
		for file in range(8):
			for rank in range(8):
				#Removes checks to re-add them later
				board[file][rank][y] = False
				board[file][rank][x] = False
				if board[file][rank][0] != False:
					if colour == True and board[file][rank][0][:1] == 'W' or colour == False and board[file][rank][0][:1] == 'B':
						if board[file][rank][0][2:] == 'Pawn':
							checks.append(self.pawn.get_attacks(file, rank))
						elif board[file][rank][0][2:] == 'Knight':
							checks.append(self.knight.get_attacks(file, rank))
						elif board[file][rank][0][2:] == 'Bishop':
							checks.append(self.bishop.get_attacks(board, file, rank))
						elif board[file][rank][0][2:] == 'Rook':
							checks.append(self.rook.get_attacks(board, file, rank))
						elif board[file][rank][0][2:] == 'Queen':
							checks.append(self.queen.get_attacks(board, file, rank))
						elif board[file][rank][0][2:] == 'King':
							checks.append(self.king.get_attacks(file, rank))

		#This bit adds checks from the other coloured pieces onto the board
		for i in range(len(checks)):
			for j in range(len(checks[i])):
				board[checks[i][j][0]][checks[i][j][1]][x] = True

		return board

	#Draw valid moves
	def draw_valid_moves(self, valid_moves_list):
		if len(valid_moves_list) > 0:
			for i in range(len(valid_moves_list)):
				pygame.draw.circle(self.screen, ' dark grey', (valid_moves_list[i][0] * 90 + 135, valid_moves_list[i][1] * 90 + 45), 15)

	#Gets all valid remaining moves
	def get_all_remaining_valid_moves(self, board, colour, prev_board, castle_array):

		remaining_moves = []

		if colour == True:
			col = 'W'
		else:
			col = 'B'

		for file in range(8):
			for rank in range(8):

				if board[file][rank][0] != False:
					if board[file][rank][0][0] == col:
						self.set_valid_moves(board, colour, file, rank, prev_board, castle_array)
						self.check_if_legal_move(board, colour, file, rank)
						for i in range(len(self.valid_moves_list)):
							remaining_moves.append(self.valid_moves_list[i])

		return remaining_moves

	#Checks to see which moves can be made without the king getting in check
	def check_if_legal_move(self, board, colour, mouse_x, mouse_y):
		if colour == True:
			x = 2
			col = 'W'
		else:
			x = 1
			col = 'B'

		#To ensure that the for loop works correctly
		temp_moves_list = []
		for i in range(len(self.valid_moves_list)):
			temp_moves_list.append(self.valid_moves_list[i])

		#Gets the valid move list and flips the board to get checks
		if board[mouse_x][mouse_y][0] != False:
			for i in range(len(temp_moves_list)):

				#This for loop insures that the board IS.NOT.REFERENCED.IN.ANY.WAY
				temp_board = [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]
				for file in range(8):
					for rank in range(8):
						for row in range(3):
							temp_board[file][rank].append(board[file][rank][row])

				#Moves piece to next moves position
				temp = temp_board[mouse_x][mouse_y][0]
				temp_board[temp_moves_list[i][0]][temp_moves_list[i][1]][0] = temp
				temp_board[mouse_x][mouse_y][0] = False
				#Flips the board and gets checks
				temp_board = self.flip_board(temp_board)
				temp_board = self.get_all_relevant_checks(temp_board, not colour)

				#Finds the king's position and checks to see if it is in check
				for kx in range(8):
					for ky in range(8):
						if temp_board[kx][ky][x] == True and temp_board[kx][ky][0] != False and temp_board[kx][ky][0][0] == col:
							if temp_board[kx][ky][0][2:] == 'King':
								#Pops the right value (hopefully)
								pointer = 0
								while self.valid_moves_list[pointer] != temp_moves_list[i] and pointer < len(self.valid_moves_list):
									pointer += 1
								if self.valid_moves_list[pointer] == temp_moves_list[i]:
									self.valid_moves_list.pop(pointer)

	#Gets all of the possible moves, looks for stalemate
	def get_all_moves(self, board, colour):

		#Moves array
		moves = []
		remaining_moves = []

		#Loops through the board
		for file in range(8):
			for rank in range(8):
				if board[file][rank][0] != False:
					if colour == True and board[file][rank][0][:1] == 'W' or colour == False and board[file][rank][0][:1] == 'B':
						if board[file][rank][0][2:] == 'Pawn':
							self.pawn.valid_moves(file, rank, board, colour)
							moves.append(self.pawn.get_valid_moves())
						elif board[file][rank][0][2:] == 'Knight':
							self.knight.valid_moves(file, rank, board, colour)
							moves.append(self.knight.get_valid_moves())
						elif board[file][rank][0][2:] == 'Bishop':
							self.bishop.valid_moves(file, rank, board, colour)
							moves.append(self.bishop.get_valid_moves())
						elif board[file][rank][0][2:] == 'Rook':
							self.rook.valid_moves(file, rank, board, colour)
							moves.append(self.rook.get_valid_moves())
						elif board[file][rank][0][2:] == 'Queen':
							self.queen.valid_moves(file, rank, board, colour)
							moves.append(self.queen.get_valid_moves())
						elif board[file][rank][0][2:] == 'King':
							self.king.valid_moves(file, rank, board, colour)
							moves.append(self.king.get_valid_moves())

		#This bit adds checks from the other coloured pieces onto the board
		for i in range(len(moves)):
			for j in range(len(moves[i])):
				remaining_moves.append(moves[i][j])

		return remaining_moves

	#Changes the occupance position of pieces on board
	def move_piece(self, board, colour, selected_piece, mouse_x, mouse_y):

		#en peasant
		if self.pawn.get_en_peasant() == True and mouse_y < 7:
			name = board[selected_piece[0]][selected_piece[1]][0]
			board[selected_piece[0]][selected_piece[1]][0] = False
			board[mouse_x][mouse_y][0] = name
			board[mouse_x][mouse_y + 1][0] = False

		#Castling Left
		elif board[selected_piece[0]][selected_piece[1]][0][2:] == 'King' and selected_piece[0] - mouse_x == 2:
			name = board[selected_piece[0]][selected_piece[1]][0]
			board[selected_piece[0]][selected_piece[1]][0] = False
			board[mouse_x][mouse_y][0] = name
			name = board[0][7][0]
			board[0][7][0] = False
			board[mouse_x + 1][mouse_y][0] = name

		#Caaslting Left
		elif board[selected_piece[0]][selected_piece[1]][0][2:] == 'King' and selected_piece[0] - mouse_x == -2:
			name = board[selected_piece[0]][selected_piece[1]][0]
			board[selected_piece[0]][selected_piece[1]][0] = False
			board[mouse_x][mouse_y][0] = name
			name = board[7][7][0]
			board[7][7][0] = False
			board[mouse_x - 1][mouse_y][0] = name
		#Normal move
		else:
			name = board[selected_piece[0]][selected_piece[1]][0]
			board[selected_piece[0]][selected_piece[1]][0] = False
			board[mouse_x][mouse_y][0] = name

		self.get_all_relevant_checks(board, colour)
		self.pawn.set_en_peasant(False)
		
		return board

	#Sets all of the valid moves <---- needs some work
	def set_valid_moves(self, board, colour, mouse_x, mouse_y, prev_board, castle_array):
		if board[mouse_x][mouse_y][0][2:] == 'Pawn':
			self.pawn.valid_moves(mouse_x, mouse_y, board, colour, prev_board)
			self.valid_moves_list = self.pawn.get_valid_moves()
			self.selected_piece = [mouse_x, mouse_y]

		elif board[mouse_x][mouse_y][0][2:] == 'Knight':
			self.knight.valid_moves(mouse_x, mouse_y, board, colour)
			self.valid_moves_list = self.knight.get_valid_moves()
			self.selected_piece = [mouse_x, mouse_y]

		elif board[mouse_x][mouse_y][0][2:] == 'Bishop':
			self.bishop.valid_moves(mouse_x, mouse_y, board, colour)
			self.valid_moves_list = self.bishop.get_valid_moves()
			self.selected_piece = [mouse_x, mouse_y]

		elif board[mouse_x][mouse_y][0][2:] == 'Rook':
			self.rook.valid_moves(mouse_x, mouse_y, board, colour)
			self.valid_moves_list = self.rook.get_valid_moves()
			self.selected_piece = [mouse_x, mouse_y]

		elif board[mouse_x][mouse_y][0][2:] == 'Queen':
			self.selected_piece = [mouse_x, mouse_y]
			self.queen.valid_moves(mouse_x, mouse_y, board, colour)
			self.valid_moves_list = self.queen.get_valid_moves()

		elif board[mouse_x][mouse_y][0][2:] == 'King':
			self.selected_piece = [mouse_x, mouse_y]
			self.king.valid_moves(mouse_x, mouse_y, board, colour, castle_array)
			self.valid_moves_list = self.king.get_valid_moves()

	#Gets valid moves
	def get_valid_moves(self):
		return self.valid_moves_list

	#Gets selected piece
	def get_selected_piece(self):
		return self.selected_piece

	def get_for_prev_board(self, board):
		prev_board = [[[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []], [[], [], [], [], [], [], [], []]]
		for file in range(8):
			for rank in range(8):
				for row in range(3):
					prev_board[file][rank].append(board[file][rank][row])
		return prev_board

	#Pawn promotion
	def promotion(self, board, screen, colour, x_pos):

		#Temp mouse position variables
		mouse_x, mouse_y = False, False

		#Running condition
		running = True

		while running == True:

			if colour == True:
				x = 'W_'
			else:
				x = 'B_'

			#Draws the board to show new move
			self.screen.fill((221, 187, 207))

			#Pygame event thing
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					return False
				if event.type == pygame.MOUSEBUTTONDOWN:#Checks for clicks
					mousePosOnClick = pygame.mouse.get_pos()
					mouse_x, mouse_y = mousePosOnClick[0] // 90 - 1, mousePosOnClick[1] // 90

			if mouse_x == -1 and (mouse_y == 0 or mouse_y == 1 or mouse_y == 2 or mouse_y == 3):
				if mouse_y == 0:
					board[x_pos][0][0] = x + 'Queen'
				elif mouse_y == 1:
					board[x_pos][0][0] = x + 'Rook'
				elif mouse_y == 2:
					board[x_pos][0][0] = x + 'Bishop'
				elif mouse_y == 3:
					board[x_pos][0][0] = x + 'Knight'

				return board

			if running == True:

				self.draw_board(colour, True)
				self.draw_piece(board)

				#Draw the pieces which can be selected
				self.screen.blit(self.images[x + 'Queen'],(0, 0))
				self.screen.blit(self.images[x + 'Rook'],(0, 90))
				self.screen.blit(self.images[x + 'Bishop'],(0, 180))
				self.screen.blit(self.images[x + 'Knight'],(0, 270))

				pygame.display.flip()