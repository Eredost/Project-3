#-*- coding:UTF-8 -*-

import pygame
from pygame.locals import *

from Level import *
from Character import *

#INITIALISE PYGAME WINDOW
pygame.init()
window = pygame.display.set_mode((window_size,window_size))

#LOADING ICON AND TITLE OF WINDOW
icon = pygame.image.load(window_icon)
pygame.display.set_caption(window_title)
pygame.display.set_icon(icon)

#LOADING LEVEL SPRITES
level = Level("Niveau.txt")
level.world_generator()
level.display(window)
pygame.display.update()

#LOADING GAME CHARACTERS
Mcgyver = Character(window_icon, level)
window.blit(Mcgyver.character, (Mcgyver.pos_x, Mcgyver.pos_y))
guardian = pygame.image.load(guardian_pic).convert_alpha()

#REFRESH THE SCREEN
pygame.display.flip()

keep_on = 1

#LOOP
while keep_on == 1 :

	pygame.time.Clock().tick(30)

	for event in pygame.event.get() :
		if event.type == QUIT :
			keep_on = 0

		elif event.type == KEYDOWN:
				
				#ARROWS KEYS FOR MOVING THE CHARACTER
				if event.key == K_RIGHT:
					Mcgyver.move('right')
				
				elif event.key == K_LEFT:
					Mcgyver.move('left')
				
				elif event.key == K_UP:
					Mcgyver.move('up')
				
				elif event.key == K_DOWN:
					Mcgyver.move('down')

	
	#REFRESH CHARACTERS AND OBJECTS ON WINDOW				
	level.display(window)
	window.blit(guardian,(560,80))
	window.blit(Mcgyver.character, (Mcgyver.pos_x, Mcgyver.pos_y))
	pygame.display.flip()
	