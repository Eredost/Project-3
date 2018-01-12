#-*-coding:UTF-8 -*-

import pygame
from pygame.locals import *
from Constantes import *

class Level:
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def world_generator(self):
		#PASS THE TEXT FILE IN PARAMETER AND SAVE ALL CORRESPONDING LETTERS IN A LIST
		with open("Niveau.txt", "r") as fichier :
			level_structure = []
			
			for ligne in fichier :
				line_level = []

				for sprite in ligne :

					if sprite != "\n" :

						line_level.append(sprite)

				level_structure.append(line_level)

			self.structure = level_structure

	def display(self, window):

		#LOADING AND CUTING ALL PICTURES FOR LABYRINTH
		walls = pygame.image.load(wall_pic)
		ground = pygame.image.load(ground_pic)
		horizontal_wall = walls.subsurface(160,0,40,40).convert()
		vertical_wall = walls.subsurface(260,120,40,40).convert()
		ne_corner_wall = walls.subsurface(400,120,40,40).convert()
		nw_corner_wall = walls.subsurface(440,120,40,40).convert()
		se_corner_wall = walls.subsurface(400,80,40,40).convert()
		sw_corner_wall = walls.subsurface(440,80,40,40).convert()
		middle_wall = walls.subsurface(300,20,40,40).convert()
		floor_tile = ground.subsurface(300,60,20,20).convert()

		line_num = 0
		i = 0

		for line in self.structure:
			case_num = 0
			for sprite in line:
				x = case_num * sprite_size
				y = line_num * sprite_size
				#ADDING SPRITES TO THE LEVEL
				if sprite in "X" :
					
					if self.structure[line_num - 1][case_num] == "X" and self.structure[line_num + 1][case_num] == "X" :
						window.blit(vertical_wall, (x,y))

					elif self.structure[line_num][case_num - 1] == "X" and self.structure[line_num][case_num + 1] == "X" :
						window.blit(horizontal_wall, (x,y))

					elif self.structure[line_num - 1][case_num] == "X" and self.structure[line_num][case_num + 1] == "X" :
						window.blit(sw_corner_wall, (x,y))

					elif self.structure[line_num][case_num + 1] == "X" and self.structure[line_num + 1][case_num] == "X" :
						window.blit(nw_corner_wall, (x,y))

					elif self.structure[line_num + 1][case_num] == "X" and self.structure[line_num][case_num - 1] == "X" :
						window.blit(ne_corner_wall, (x,y))

					elif self.structure[line_num][case_num - 1] == "X" and self.structure[line_num - 1][case_num] == "X" :
						window.blit(se_corner_wall, (x,y))

					else :
						window.blit(middle_wall, (x,y))



				elif sprite != "#" :		   
					window.blit(floor_tile, (x,y))
					window.blit(floor_tile, (x+20,y))
					window.blit(floor_tile, (x,y+20))
					window.blit(floor_tile, (x+20,y+20))

				
				case_num += 1
			line_num += 1