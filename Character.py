#-*-coding:UTF-8 -*-
"""This module create a playable character
with different mechanics, like move and check
his position on interface"""

import pygame
from pygame.locals import *

from Constantes import *
from Level import *


class Character:
    """This class create the character and setup
    all his mechanics"""

    def __init__(self, character, level):
        """Loading sprite of the character and
        and we implant it as its initial position"""

        self.character = pygame.image.load(character).convert_alpha()
        self.level = level
        self.case_x = self.level.character_a_pos[0] // SPRITE_SIZE
        self.case_y = self.level.character_a_pos[1] // SPRITE_SIZE
        self.pos_x = self.level.character_a_pos[0]
        self.pos_y = self.level.character_a_pos[1]

    def move(self, direction):
        """The x and y position of the character
        is adjusted according to the player's choice"""

        if direction == "right":

            if self.case_x < (SPRITE_NUMBER - 1):

                if self.level.structure[self.case_y][self.case_x+1] not in "#X/":

                    self.case_x += 1
                    self.pos_x = self.case_x * SPRITE_SIZE

        if direction == "left":

            if self.case_x > 0:

                if self.level.structure[self.case_y][self.case_x-1] not in "#X/":

                    self.case_x -= 1
                    self.pos_x = self.case_x * SPRITE_SIZE

        if direction == "up":

            if self.case_y > 0:

                if self.level.structure[self.case_y-1][self.case_x] not in "#X/":

                    self.case_y -= 1
                    self.pos_y = self.case_y * SPRITE_SIZE

        if direction == "down":

            if self.case_y < (SPRITE_NUMBER - 1):

                if self.level.structure[self.case_y+1][self.case_x] not in "X#/":

                    self.case_y += 1
                    self.pos_y = self.case_y * SPRITE_SIZE
