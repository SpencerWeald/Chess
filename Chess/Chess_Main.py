#Important imports
import pygame, time

#Importing important classes
from Chess_Board import Board
from Pieces import Pawn
from Pieces import Knight
from Pieces import Bishop
from Pieces import Rook
from Pieces import Queen
from Pieces import King

#Initialsises
pygame.init()
clock = pygame.time.Clock()

#Main class to run the fundamentals 
class Main():

	#Initialsies properties
	def __init__(self):
		#Sets dimensions, window title, board
		self.width, self.height = 810, 810
		self.screen = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption('Chess')
		self.board_class = Board(self.screen)
		self.board_class.create_board()
		self.board = self.board_class.get_board()

		#Clears file
		file = open('draw_by_repetition.txt', 'w')
		file.write('')
		file.close()

		#Starts recording board positions for draw
		self.new = []
		for file in range(8):
			for rank in range(8):
				self.new.append(self.board[file][rank][0])
		self.clear_board()

		self.mouse_x = -1
		self.mouse_y = -1

		#Stalemate variable
		self.remaining_moves = ['lol']

		#Valid moves
		self.valid_moves_list = []

		#Keeps track of which piece has been clicked
		self.selected_piece = ''

		#Initialise piece class
		self.pawn = Pawn()
		self.knight = Knight()
		self.bishop = Bishop()
		self.rook = Rook()
		self.queen = Queen()
		self.king = King()

		#Variable to keep track of when to append to file and when to clear it
		self.total_piece_number = 32

		#Used for en peasant
		self.prev_board = self.board

		#Casting variables
		self.w_king_move = False
		self.b_king_move = False
		self.l_w_rook_move = False
		self.r_w_rook_move = False
		self.l_b_rook_move = False
		self.r_b_rook_move = False

		self.castle_array = [self.w_king_move, self.b_king_move, self.l_w_rook_move, self.r_w_rook_move, self.l_b_rook_move, self.r_b_rook_move]

		#Running condition
		self.running = True

	#Runs the screen
	def run(self):

		#Colour of board, True = White, False = Black
		self.colour = True

		#Loop
		while self.running == True:

			#Draws the screen
			self.screen = pygame.display.set_mode((self.width, self.height))
			#Fill background
			self.screen.fill((221, 187, 207))

			#Resest all valid moves
			self.valid_moves = []

			self.board_class.draw_board(self.colour, False)

			self.board_class.draw_piece(self.board), self.board_class.draw_valid_moves(self.valid_moves_list)

			#Pygame event thing
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.MOUSEBUTTONDOWN:#Checks for clicks
					self.mousePosOnClick = pygame.mouse.get_pos()
					self.mouse_x, self.mouse_y = self.mousePosOnClick[0] // 90 - 1, self.mousePosOnClick[1] // 90

					if self.mouse_x < 8 and self.mouse_x > -1 and self.mouse_y < 8 and self.mouse_y > -1:
						self.manage_click()

			pygame.display.flip()

			clock.tick(60)

		#Draws the board again in case of a type of mate

		#Fill background
		self.screen.fill((221, 187, 207))

		self.board_class.draw_board(self.colour, False)
		self.board_class.draw_piece(self.board)
		pygame.display.flip()
		time.sleep(0.5)


	#Manages clicks
	def manage_click(self):

		#Checks to see if a valid move square has been selected
		skip_piece_select = False
		if len(self.valid_moves_list) > 0:
			for i in range(len(self.valid_moves_list)):
				if self.valid_moves_list[i][0] == self.mouse_x and self.valid_moves_list[i][1] == self.mouse_y:
					skip_piece_select = True

		#Moves the piece
		if skip_piece_select == True:

			#Casting variables
			w_king_move = False
			b_king_move = False
			l_w_rook_move = False
			r_w_rook_move = False
			l_b_rook_move = False
			r_b_rook_move = False

			#Gets the previous (current) board for the next move
			self.board = self.board_class.flip_board(self.board)
			self.prev_board = self.board_class.get_for_prev_board(self.board)
			self.board = self.board_class.flip_board(self.board)

			#Checks for king move #Keeps going throught these statments even after it has done it once, no biggie, just a lil annoying
			if self.board[self.selected_piece[0]][self.selected_piece[1]][0][2:] == 'King':
				if self.colour == True:
					w_king_move = True
				else:
					b_king_move = True

			#Checks for left and right rook move #Keeps going throught these statments even after it has done it once, no biggie, just a lil annoying
			if self.board[self.selected_piece[0]][self.selected_piece[1]][0][2:] == 'Rook':
				if self.selected_piece[0] == 0:
					if self.colour == True:
						l_w_rook_move = True
					else:
						l_b_rook_move = True
				elif self.selected_piece[0] > 0:
					if self.colour == True:
						r_w_rook_move = True
					else:
						r_b_rook_move = True

			#Moves piece
			self.board = self.board_class.move_piece(self.board, self.colour, self.selected_piece, self.mouse_x, self.mouse_y)

			#Draws the board to show new move
			self.screen.fill((221, 187, 207))

			self.board_class.draw_board(self.colour, False)
			self.board_class.draw_piece(self.board)
			pygame.display.flip()

			time.sleep(0.1)

			#No mo castling
			if w_king_move == True:
				self.w_king_move = True
			if b_king_move == True:
				self.b_king_move = True

			if l_w_rook_move == True:
				self.l_w_rook_move = True
			if r_w_rook_move == True:
				self.r_w_rook_move = True

			if l_b_rook_move == True:
				self.l_b_rook_move = True
			if r_b_rook_move == True:
				self.r_b_rook_move = True

			#Updates castle_array
			self.castle_array = [self.w_king_move, self.b_king_move, self.l_w_rook_move, self.r_w_rook_move, self.l_b_rook_move, self.r_b_rook_move]

			for i in range(8):
				if self.board[i][0][0] != False:
					if self.board[i][0][0][2:] == 'Pawn':
						temp = self.board_class.promotion(self.board, self.screen, self.colour, i)

						if temp == False:
							self.running = False
							break
						else:
							self.board = temp

							#Draws the board to show new move
							self.screen.fill((221, 187, 207))

							self.board_class.draw_board(self.colour, False)
							self.board_class.draw_piece(self.board)
							pygame.display.flip()

							time.sleep(0.1)

			#So it doesn't flip the board when quitting
			if self.running == True:

				#Flips the board
				self.colour = not self.colour
				self.board = self.board_class.flip_board(self.board)

				#Gets important move data
				self.remaining_moves = self.board_class.get_all_remaining_valid_moves(self.board, self.colour, self.prev_board, self.castle_array)
				self.selected_piece = ''
				self.valid_moves_list = []

				#Draw and checkmate conditions
				self.mate()
				time.sleep(0.1)

		#If no valid move tile has been seleceted (while a piece has also been selected keep in mind)
		else:
			if self.board[self.mouse_x][self.mouse_y][0] != False:
				#Makes sure that the correct piece/squares are pressed
				if self.colour == True and self.board[self.mouse_x][self.mouse_y][0][:1] == 'W' or self.colour == False and self.board[self.mouse_x][self.mouse_y][0][:1] == 'B':
					self.board_class.set_valid_moves(self.board, self.colour, self. mouse_x, self.mouse_y, self.prev_board, self.castle_array)
					self.board_class.check_if_legal_move(self.board.copy(), self.colour, self.mouse_x, self.mouse_y)
					self.valid_moves_list = self.board_class.get_valid_moves()
					self.selected_piece = self.board_class.get_selected_piece()

				#Resets variables in case no valid move wants to be made
				else:
					self.selected_piece = ''
					self.valid_moves_list = []

			#Resets variables in case no valid move wants to be made
			else:
				self.selected_piece = ''
				self.valid_moves_list = []

	#Different mating conditions
	def mate(self):

		#Makes sure you can't get two types of mates at once
		mated = False

		if self.colour == True:
			x = 2
			col = 'W'
			player = 'Black'
		else:
			x = 1
			col = 'B'
			player = 'White'

		for file in range(8):
			for rank in range(8):

				if self.board[file][rank][x] == True and self.board[file][rank][0] != False and self.board[file][rank][0][0] == col and self.board[file][rank][0][2:] == 'King' and len(self.remaining_moves) == 0:
					self.running = False
					mated = True
					print(player,'wins by checkmate')
					#time.sleep(10)


		#Draw Condition
		if len(self.remaining_moves) == 0 and mated == False:
			self.running = False
			print('Draw by stalemate')

		if mated == False:
			if self.colour == False:
				self.board = self.board_class.flip_board(self.board)
			self.new = []
			for file in range(8):
				for rank in range(8):
					self.new.append(self.board[file][rank][0])
			self.pieces_count()
			self.draw_by_repetition()
			if self.colour == False:
				self.board = self.board_class.flip_board(self.board)

	#Clears the file and writes the board to it once
	def clear_board(self):
		file = open('draw_by_repetition.txt', 'w')
		file.write(str(self.new) + '\n')
		file.close()

	#Appends the board onto the existing boards in the file
	def append_board(self):
		file = open('draw_by_repetition.txt', 'a')
		file.write(str(self.new) + '\n')
		file.close()

	#Loops through the board and if the same board is repeated three times then the game is a draw
	def draw_by_repetition(self):
		count = 0
		file = open('draw_by_repetition.txt', 'r')
		for line in file.readlines():
			line = line.replace('/n','')
			line = line.replace('[', '')
			line = line.replace(']', '')
			line = line.replace(' ','')
			line = line.split(',')
			for i in range(64):
				line[i] = line[i].strip()
				if line[i] == 'False':
					line[i] = False
				elif line[i] == 'True':
					line[i] = True
				elif line[i] == "'B_Pawn'":
					line[i] = 'B_Pawn'
				elif line[i] == "'W_Pawn'":
					line[i] = 'W_Pawn'
				elif line[i] == "'B_Knight'":
					line[i] = 'B_Knight'
				elif line[i] == "'W_Knight'":
					line[i] = 'W_Knight'
				elif line[i] == "'B_Bishop'":
					line[i] = 'B_Bishop'
				elif line[i] == "'W_Bishop'":
					line[i] = 'W_Bishop'
				elif line[i] == "'B_Rook'":
					line[i] = 'B_Rook'
				elif line[i] == "'W_Rook'":
					line[i] = 'W_Rook'
				elif line[i] == "'B_Queen'":
					line[i] = 'B_Queen'
				elif line[i] == "'W_Queen'":
					line[i] = 'W_Queen'
				elif line[i] == "'B_King'":
					line[i] = 'B_King'
				elif line[i] == "'W_King'":
					line[i] = 'W_King'

			if line == self.new:
				count += 1

		file.close()

		if count == 3:
			self.running = False
			print('Draw by repetition')

	#Counts the amount of pieces in the board and calls the correct function
	def pieces_count(self):
		count = 0
		for file in range(8):
			for rank in range(8):
				if self.board[file][rank][0]:
					count += 1

		if count == self.total_piece_number:
			self.append_board()
		else:
			self.total_piece_number = count
			self.clear_board()

#Runs the progrom
go = Main()
go.run()

pygame.quit()

#Things still to do: win screen (optional)

#Current board array: [piece name, attacked by white, attacked by black] + new field of moves made by piece (for en peasant if required)