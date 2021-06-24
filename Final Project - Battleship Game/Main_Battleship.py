#Thomas Rowley
#6/23/2021 - beginning to work on basic grid and menu


import random, time, datetime, pygame, sys, os, math

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

#block width
blockWIDTH= 1

def levelONE():
    screen.fill(BLACK)
    drawGRID()

def levelTWO():
    screen.fill(BLACK)
    drawGRID()

def levelTHREE():
    screen.fill(BLACK)
    drawGRID()

def menu():
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

    quitTEXT= "Quit"
    quitFONTTEXT= mainFONT.render(quitTEXT, 1, SPY_GREEN)
    rect4= pygame.Rect((WIDTH/2 - quitFONTTEXT.get_width()/2), 375, 135, 75)
    pygame.draw.rect(screen, BLACK, rect4)
    screen.blit(quitFONTTEXT, (WIDTH/2 - quitFONTTEXT.get_width()/2, 375))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if rect1.collidepoint((mx, my)):
                levelONE()
            if rect2.collidepoint((mx, my)):
                levelTWO()
            if rect3.collidepoint((mx, my)):
                levelTHREE()
            if rect4.collidepoint((mx, my)):
                pygame.quit()
    pygame.display.update()

#grid created by using, https://stackoverflow.com/questions/33963361/how-to-make-a-grid-in-pygame
def drawGRID():
    blockSIZE= 80
    for x in range(0, WIDTH, blockSIZE):
        for y in range(0, HEIGHT, blockSIZE):
            rect= pygame.Rect(x, y, blockSIZE, blockSIZE)
            pygame.draw.rect(screen, SPY_GREEN, rect, blockWIDTH)


check= True
while check:
    menu()
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check= False





    pygame.display.update()
pygame.quit()