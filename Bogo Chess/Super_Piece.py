import pygame

#General method that each piece will need
class Super_Piece():

	#Returns all of the valid moves for a selected piece
	def get_valid_moves(self):
		return self.valid_moves_list