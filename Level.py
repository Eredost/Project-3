#-*-coding:UTF-8 -*-
"""This module convert a text file full of "X" for walls
and whitespaces for floor to transform into a graphical
playable interface"""

import pygame
from pygame.locals import *

from Constantes import *


class  Level:
    """Loading text file to turn it
    into a graphical user interface"""

    def __init__(self, fichier):
        """Loading text file taken
        as a parameter"""

        self.fichier = fichier
        self.structure = 0

    def world_generator(self):
        """It loads the contents of the text file
       for inclusion in a list and use it later"""

        with open("Niveau.txt", "r") as fichier:
            level_structure = []
            for ligne in fichier:
                line_level = []

                for sprite in ligne:

                    if sprite != "\n":

                        line_level.append(sprite)

                level_structure.append(line_level)

            self.structure = level_structure

    def display(self, window):
        """Cutting the images to get the sprites
       and according to the place in the list of
       elements, we add the corresponding sprite"""

        walls = pygame.image.load(wall_pic)
        ground = pygame.image.load(ground_pic)
        horizontal_wall = walls.subsurface(160, 0, 40, 40).convert()
        vertical_wall = walls.subsurface(260, 120, 40, 40).convert()
        ne_corner_wall = walls.subsurface(400, 120, 40, 40).convert()
        nw_corner_wall = walls.subsurface(440, 120, 40, 40).convert()
        se_corner_wall = walls.subsurface(400, 80, 40, 40).convert()
        sw_corner_wall = walls.subsurface(440, 80, 40, 40).convert()
        middle_wall = walls.subsurface(300, 20, 40, 40).convert()
        floor_tile = ground.subsurface(300, 60, 20, 20).convert()
        line_num = 0

        for line in self.structure:
            case_num = 0
            for sprite in line:
                pos_x = case_num * sprite_size
                pos_y = line_num * sprite_size
                if sprite in "X":
                    if self.structure[line_num - 1][case_num] == "X" and \
                            self.structure[line_num + 1][case_num] == "X":
                        window.blit(vertical_wall, (pos_x, pos_y))

                    elif self.structure[line_num][case_num - 1] == "X" and \
                            self.structure[line_num][case_num + 1] == "X":
                        window.blit(horizontal_wall, (pos_x, pos_y))

                    elif self.structure[line_num - 1][case_num] == "X" and \
                            self.structure[line_num][case_num + 1] == "X":
                        window.blit(sw_corner_wall, (pos_x, pos_y))

                    elif self.structure[line_num][case_num + 1] == "X" and \
                            self.structure[line_num + 1][case_num] == "X":
                        window.blit(nw_corner_wall, (pos_x, pos_y))

                    elif self.structure[line_num + 1][case_num] == "X" and \
                            self.structure[line_num][case_num - 1] == "X":
                        window.blit(ne_corner_wall, (pos_x, pos_y))

                    elif self.structure[line_num][case_num - 1] == "X" and \
                            self.structure[line_num - 1][case_num] == "X":
                        window.blit(se_corner_wall, (pos_x, pos_y))

                    else:
                        window.blit(middle_wall, (pos_x, pos_y))

                elif sprite != "#":
                    window.blit(floor_tile, (pos_x, pos_y))
                    window.blit(floor_tile, (pos_x+20, pos_y))
                    window.blit(floor_tile, (pos_x, pos_y+20))
                    window.blit(floor_tile, (pos_x+20, pos_y+20))

                case_num += 1
            line_num += 1
