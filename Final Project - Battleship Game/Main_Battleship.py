#Thomas Rowley
#6/23/2021 - beginning to work on basic grid and menu


import random, time, datetime, pygame, sys, os, math
import threading
from pygame.constants import MOUSEBUTTONDOWN

from pygame.time import Clock

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
RED= [255, 0, 0]

screen.fill(BLACK)
pygame.display.update()

mainFONT= pygame.font.Font("Final Project - Battleship Game\military_font_7.ttf", 60)

#block width
blockWIDTH= 1

#clock for scores
clock= pygame.time.Clock()

blockLIST= []
def drawGRID():
    blockSIZE= 80
    for x in range(0, WIDTH, blockSIZE):
        for y in range(0, HEIGHT, blockSIZE):
            rect= pygame.Rect(x, y, blockSIZE, blockSIZE)
            check= bool(random.getrandbits(1))
            blockLIST.append([rect, check])
            pygame.draw.rect(screen, SPY_GREEN, rect, blockWIDTH)
    print(blockLIST)

def levelONE():
    screen.fill(BLACK)
    drawGRID()
    pygame.display.update()
    """ for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type== MOUSEBUTTONDOWN:
            mx, my =pygame.mouse.get_pos() 
            for squares in blockLIST: 
                rect, check= squares
                if check:
                    if rect.collidepoint(mx, my):
                        pygame.draw.rect(screen, RED, rect)
                        blockLIST[1] = False
    """
    #pygame.display.update()
    
    # pygame.time.Clock()
    # pygame.time.Clock.tick()

def advanceToLevel():
    screen.fill(BLACK)
    drawGRID()
    pygame.display.update()
    #time.sleep(100)

def levelTWO():
    screen.fill(BLACK)
    drawGRID()
    pygame.display.update()
    time.sleep(100)

def levelTHREE():
    screen.fill(BLACK)
    drawGRID()
    pygame.display.update()
    time.sleep(100)

def recordSCORE():
    file= "Battleship_Scores.txt"
    FILE= open(file, "w")
    FILE.write("************BATTLESHIP SCORES************")

def menu():
    screen.fill(BLACK)
    gameTEXT= "Battleship Game"
    gameFONTTEXT= mainFONT.render(gameTEXT, 1, SPY_GREEN)
    screen.blit(gameFONTTEXT, (WIDTH/2 - gameFONTTEXT.get_width()/2, 40))

    levelONETEXT= "Level One"
    leveloneFONTTEXT= mainFONT.render(levelONETEXT, 1, SPY_GREEN)
    rect1= pygame.Rect((WIDTH/2 - leveloneFONTTEXT.get_width()/2), 150, 335, 75)
    pygame.draw.rect(screen, BLACK, rect1)
    screen.blit(leveloneFONTTEXT, (WIDTH/2 - leveloneFONTTEXT.get_width()/2, 150))

    levelTWOTEXT= "Level Two"
    leveltwoFONTTEXT= mainFONT.render(levelTWOTEXT, 1, SPY_GREEN)
    rect2= pygame.Rect((WIDTH/2 - leveltwoFONTTEXT.get_width()/2), 225, 335, 75)
    pygame.draw.rect(screen, BLACK, rect2)
    screen.blit(leveltwoFONTTEXT, (WIDTH/2 - leveltwoFONTTEXT.get_width()/2, 225))

    levelTHREETEXT= "Level Three"
    levelthreeFONTTEXT= mainFONT.render(levelTHREETEXT, 1, SPY_GREEN)
    rect3= pygame.Rect((WIDTH/2 - levelthreeFONTTEXT.get_width()/2), 300, 385, 75)
    pygame.draw.rect(screen, BLACK, rect3)
    screen.blit(levelthreeFONTTEXT, (WIDTH/2 - levelthreeFONTTEXT.get_width()/2, 300))

    scoresTEXT= "Scores"
    scoresFONTTEXT= mainFONT.render(scoresTEXT, 1, SPY_GREEN)
    rect4= pygame.Rect((WIDTH/2 - scoresFONTTEXT.get_width()/2), 375, 210, 75)
    pygame.draw.rect(screen, BLACK, rect4)
    screen.blit(scoresFONTTEXT, (WIDTH/2 - scoresFONTTEXT.get_width()/2, 375))

    quitTEXT= "Quit"
    quitFONTTEXT= mainFONT.render(quitTEXT, 1, SPY_GREEN)
    rect5= pygame.Rect((WIDTH/2 - quitFONTTEXT.get_width()/2), 450, 135, 75)
    pygame.draw.rect(screen, BLACK, rect5)
    screen.blit(quitFONTTEXT, (WIDTH/2 - quitFONTTEXT.get_width()/2, 450))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            #sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if rect1.collidepoint((mx, my)):
                t1 = threading.Thread(target=advanceToLevel, args=())
                t1.start()
            if rect2.collidepoint((mx, my)):
                t1 = threading.Thread(target=levelTWO, args=())
                t1.start()
                #levelTWO()
            if rect3.collidepoint((mx, my)):
                levelTHREE()
            if rect4.collidepoint((mx, my)):
                menu()
            if rect5.collidepoint((mx, my)):
                pygame.quit()
    pygame.display.update()

#grid created by using, https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame



check= True
while check:
    menu()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check= False
pygame.quit()
sys.exit()