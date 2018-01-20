#-*-coding:UTF-8 -*-
"""This module load items, place randomly on
the window and check the player position"""

import random

class Item:
    """This class initialize a random place
    for items and initialize it on pygame
    window, create a inventory and fills it
    according to the position of the character"""

    def __init__(self, item1, item2, item3, level, character):
        """Takes items pictures, the level where they
        will be incremented and the character to recover
        his position"""

        self.items = [item1, item2, item3]
        self.level = level
        self.character = character
        self.items_pos = []
        self.inventory = []

        #INIT RANDOM NUMBERS AND ADD IT IN A LIST TO PLACE ITEMS
        for item in self.items:

            self.items_pos.append(random.randint(0, len(self.level.blank_cases)))

    def placement(self, window):
        """We get the list of blank cases of the level and with
        the random numbers, we place them on the game window.
        We check the player position and if it is on the place
        of an object, it is added in his inventory and no longer
        display on screen"""

        value = 0

        for item in self.items:

            #WE SAVE THE POSITION X AND Y OF BLANK CASES IN VARIABLES
            blank_case_x = self.level.blank_cases[self.items_pos[value]][0]
            blank_case_y = self.level.blank_cases[self.items_pos[value]][1]

            if item not in self.inventory:

                window.blit(item, (blank_case_x, blank_case_y))

                #IF PLAYER POS IS SAME THAN ITEM POSITION
                if self.character.pos_x == blank_case_x and \
                   self.character.pos_y == blank_case_y:

                    self.inventory.append(item)

            value += 1
