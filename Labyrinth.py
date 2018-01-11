#-*- coding:UTF-8 -*-

import pygame
from pygame.locals import *
from Level import *

pygame.init()
window = pygame.display.set_mode((680,680))


level = Level("Niveau.txt")
level.world_generator()
level.display(window)
pygame.display.update()

keep_on = 1

while keep_on == 1 :

	pygame.time.Clock().tick(30)

	for event in pygame.event.get() :
		if event.type == QUIT :
			keep_on = 0
