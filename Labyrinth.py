#-*- coding:UTF-8 -*-
"""This module imports the different necessary
classes of the project and initialize the
pygame window"""

import pygame
from pygame.locals import *

from Level import *
from Character import *
from Item import *

def main():
    """This function retrieves the captured
    events (the player's actions) and puts
    the related items back on the window"""

    restart = 1

    while restart == 1:

        #INITIALISE PYGAME WINDOW
        pygame.init()
        window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

        #LOADING ICON AND TITLE OF WINDOW
        icon = pygame.image.load(WINDOW_ICON)
        pygame.display.set_caption(WINDOW_TITLE)
        pygame.display.set_icon(icon)

        #LOADING WIN AND LOOSE FONT
        font = pygame.font.SysFont('Arial', 25)

        #LOADING LEVEL SPRITES, OBJECTS AND GAME CHARACTERS
        level = Level("Levels/Level.txt")
        level.world_generator()
        level.display(window)
        mcgyver = Character(WINDOW_ICON, level)
        guardian = pygame.image.load(GUARDIAN_PIC).convert_alpha()
        objects = pygame.image.load(ITEMS)
        item_1 = objects.subsurface(96,0,32,32)
        item_2 = objects.subsurface(128,0,32,32)
        item_3 = objects.subsurface(160,0,32,32)
        items = Item(item_1, item_2, item_3, level, mcgyver)
        pygame.display.update()

        #REFRESH THE SCREEN
        pygame.display.flip()

        keep_on = 1
        restart = 0
        choice = ""

        while keep_on == 1:

            pygame.time.Clock().tick(30)

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
            window.blit(guardian, (level.character_b_pos))
            window.blit(mcgyver.character, (mcgyver.pos_x, mcgyver.pos_y))
            pygame.display.flip()

            if mcgyver.pos_x == level.finish_line_pos[0] and \
                mcgyver.pos_y == level.finish_line_pos[1]:

                if len(items.inventory) == len(items.items):
                    
                    bulle = Rect(200,250,300,300)
 
                    x_rect,y_rect = bulle.topleft
 
                    for ligne in WIN_DISPLAY.splitlines():
                        
                        x_rect,y_rect = window.blit(font.render(ligne,1,(255,255,255)),(x_rect,y_rect)).bottomleft
                        pygame.display.update(bulle)
                    keep_on = 0

                else:

                    bulle = Rect(200,250,300,300)
 
                    x_rect,y_rect = bulle.topleft
 
                    for ligne in LOOSE_DISPLAY.splitlines():
                        
                        x_rect,y_rect = window.blit(font.render(ligne,1,(255,255,255)),(x_rect,y_rect)).bottomleft
                        pygame.display.update(bulle)
                    keep_on = 0


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

if __name__ == "__main__" :
    
    main()
