#-*-coding:UTF-8 -*-
"""This module load items, place randomly on
the window and check the player position"""

import random

import pygame
from pygame.locals import *

from Constantes import *
from Level import *


class Item:

	def __init__(self, item1, item2, item3, level):
		
		self.items = [item1, item2, item3]
		self.level = level
		self.items_pos = []

		for item in self.items:
			
			self.items_pos.append(random.randint(0, len(self.level.blank_cases)))

	def placement(self, window):

		value = 0
		
		for item in self.items:
			
			window.blit(item, (self.level.blank_cases[self.items_pos[value]][0],\
							   self.level.blank_cases[self.items_pos[value]][1]))
			value += 1

