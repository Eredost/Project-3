#-*- coding:UTF-8 -*-
"""This module imports the different necessary
classes of the project and initialize the
pygame window"""

import pygame
from pygame.locals import *

from Level import Level
from Character import Character
from Item import Item
from Variables import *

def main():
    """This function retrieves the captured
    events (the player's actions) and puts
    the related items back on the window"""

    restart = 1

    #USER CHOOSE THE LEVEL HE WANT TO PLAY
    level_choice = input("Choose your level : ")

    #MAIN LOOP
    while restart == 1:

        #INITIALISE PYGAME WINDOW
        pygame.init()
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

        #LOADING ICON AND TITLE OF WINDOW
        icon = pygame.image.load(WINDOW_ICON)
        pygame.display.set_caption(WINDOW_TITLE)
        pygame.display.set_icon(icon)

        #LOADING WIN AND LOOSE DISPLAY FONT
        font = pygame.font.SysFont('Arial', 25)

        #LOADING LEVEL
        level = Level("Levels/{}".format(level_choice))
        level.world_generator()
        level.display(window)

        #LOADING CHARACTERS
        characters = pygame.image.load(CHARACTER_PIC)
        macgyver_pic = characters.subsurface(288, 0, 32, 32).convert_alpha()
        guardian_pic = characters.subsurface(224, 0, 32, 32).convert_alpha()
        mcgyver = Character(macgyver_pic, level)

        #LOADING ITEMS
        objects = pygame.image.load(ITEMS)
        item_1 = objects.subsurface(96, 0, 32, 32)
        item_2 = objects.subsurface(128, 0, 32, 32)
        item_3 = objects.subsurface(160, 0, 32, 32)
        items = Item(item_1, item_2, item_3, level, mcgyver)
        pygame.display.update()

        #REFRESH THE SCREEN
        pygame.display.flip()

        #VARIABLE TO KEEP PLAYER CHOICE LOOP
        keep_on = 1
        
        #VARIABLE USED TO RESTART GAME
        restart = 0

        #VARIABLE FOR PLAYER CHOICE TO RESTART
        choice = ""

        while keep_on == 1:

            pygame.time.Clock().tick(30)
            #CHECKING ALL PLAYERS ACTIONS (KEYS PRESSED)
            for event in pygame.event.get():
                #KEY PRESSED TO EXIT GAME
                if event.type == QUIT:
                    keep_on = 0
                    choice = "F2"

                elif event.type == KEYDOWN:

                    #ARROWS KEYS FOR MOVING THE CHARACTER
                    if event.key == K_RIGHT:
                        mcgyver.move('right')

                    elif event.key == K_LEFT:
                        mcgyver.move('left')

                    elif event.key == K_UP:
                        mcgyver.move('up')

                    elif event.key == K_DOWN:
                        mcgyver.move('down')

            #REFRESH CHARACTERS AND OBJECTS ON WINDOW
            level.display(window)
            items.placement(window)
            window.blit(guardian_pic, (level.character_b_pos))
            window.blit(mcgyver.character, (mcgyver.pos_x, mcgyver.pos_y))
            pygame.display.flip()

            if mcgyver.pos_x == level.finish_line_pos[0] and \
                mcgyver.pos_y == level.finish_line_pos[1]:

                #CREATING RECTANGLE TO CONTAIN TEXT DISPLAY
                display_rect = Rect(200, 250, 330, 300)
                x_rect, y_rect = display_rect.topleft
                
                if len(items.inventory) == len(items.items):
                    
                    for line in WIN_DISPLAY.splitlines():

                        x_rect, y_rect = window.blit(font.render(line, 1, (255, 255, 255)), \
                                                   (x_rect, y_rect)).bottomleft
                        pygame.display.update(display_rect)
                    keep_on = 0

                else:

                    for line  in LOOSE_DISPLAY.splitlines():

                        x_rect, y_rect = window.blit(font.render(line, 1, (255, 255, 255)), \
                                                   (x_rect, y_rect)).bottomleft
                        pygame.display.update(display_rect)
                    keep_on = 0

        #PLAYER'S CHOICE LOOP TO RESTART
        while choice == "":

            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                if event.type == KEYDOWN:

                    if event.key == K_F1:

                        restart = 1
                        choice = "F1"

                    if event.key == K_F2:

                        restart = 0
                        choice = "F2"

if __name__ == "__main__":

    main()
