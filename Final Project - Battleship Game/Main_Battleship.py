#Thomas Rowley
#6/23/2021 - beginning to work on basic grid and menu

from Hangman_Pygame_Fixed import TitleFont
import random, time, datetime, pygame, sys, os, math
from pygame import draw

from pygame.constants import MOUSEBUTTONDOWN

os.system("cls")
pygame.init()

#creating screen
WIDTH= 800
HEIGHT= 800

screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Battleship Game")

#Setting colors
GREY= [116, 124, 138]
WHITE= [255, 255, 255]
BLACK= [0, 0, 0]
SPY_GREEN= [21, 163, 61]

screen.fill(BLACK)
pygame.display.update()

mainFONT= pygame.font.Font("Final Project - Battleship Game\military_font_7.ttf", 60)

def menu():
    playGAMETEXT= "Battleship"
    playTEXT= mainFONT.render(playGAMETEXT, 1, SPY_GREEN)
    screen.blit(playTEXT, (WIDTH/2 - playTEXT.get_width()/2, 150))
    
    rect1= 

    mx, my = pygame.mouse.get_pos()

    if playTEXT.collidepoint((mx, my)):
         if MOUSEBUTTONDOWN:
             print("We did it.")


#grid created by using, https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
def drawGRID():
    blockSIZE= 80
    for x in range(0, WIDTH, blockSIZE):
        for y in range(0, HEIGHT, blockSIZE):
            rect= pygame.Rect(x, y, blockSIZE, blockSIZE)
            pygame.draw.rect(screen, SPY_GREEN, rect, 1)


check= True
while check:
    menu()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check= False





    pygame.display.update()
pygame.quit()