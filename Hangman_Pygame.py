#Thomas Rowley
#Create a hangman version of the game
#Use images in a list, use fonts and render them

from Word_Game_1_In_Class import updateWORD
import pygame, math, random, sys, time, os

os.system("cls")
pygame.init()

#create out screen or window

WIDTH= 800
HEIGHT= 500
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

#Define colors
WHITE= [255, 255, 255]
BLACK= [0, 0, 0]

#setting the color of the screen
screen.fill(WHITE)
pygame.display.update()

#Load images
images= []
for i in range(7):
    image= pygame.image.load("ImagesHM\hangman" + str(i) + (".png"))
    images.append(image)
    #screen.blit(images[i], (80, 100))

#Words list
playersLIST= ["Lebron", "MJ", "Curry", "KD", "Granger", "Kobe", "Kareem", "Magic", "Hakeem", "Oscar", "Dirk", "Luka"]

#set up fonts
titleFONT= pygame.font.SysFont("comicsans", 70)
wordFONT= pygame.font.SysFont("comicsans", 50)
#function to update game and screen
def updateSCREEN(displayWord):
    screen.fill(WHITE)
    screen.blit(images[turns], (80, 100))
    pygame.display.update()
    pygame.time.delay(500)
    textW= wordFONT.render(displayWord, 1, BLACK)
    screen.blit(textW, (350, 150))
    text= titleFONT.render("HANGMAN", 1, BLACK)
    centerTITLE= WIDTH/2-text.get_width()/2  #gets the width of my screen/2 - width of our text
    screen.blit(text, (centerTITLE, 20))
    screen.blit(images[turns], (80, 100))
    pygame.display.update()

def updateWord(word, guesses, turns):  # function with a parameter to update word
    displayWord= ""
    for char in word:
        if char in guesses:
            print(char,end=' ')
            displayWord += char+" "
        else:
            displayWord += "_ "
            print('_', end =' ')
    return displayWord

check= True

while check:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            check= False
    word= random.choice(playersLIST)
    counter= len(word)
    turns= 0  # should we consider controlling this number when he/she misses?
    guesses=""
    displayWord= updateWORD(word, guesses)
    updateSCREEN(displayWord, turns)
    
    while turns<7 and counter >0:
        newGuess=input("\n\n Give me a letter ")
            #check that the new letter has not been used before
        if newGuess not in guesses:
            if newGuess not in word:
                turns +=1    #       turns = turns -1
                print("Wrong! You have  ", turns, "guesses left")
            else:
                counter -=word.count(newGuess) #delete repeated letters
                print("nice guess!")
            guesses += newGuess 
        else:
            print("you used this one already")
        updateWord(word, guesses, turns)
        #end of whole loop with 
pygame.quit()
sys.exit()

