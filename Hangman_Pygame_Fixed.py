# Thomas Rowley

# Create a HNagman version of the game: 

# Use images in a listUse Fonts, render them 

 
 

import pygame, math, random, sys, time, os 

 
 

#os.system('cls') 

pygame.init() 

 
 

#create our screen or window 

 
 

WIDTH=800 

HEIGHT=500 

screen = pygame.display.set_mode((WIDTH,HEIGHT))  

pygame.display.set_caption("Hangman Game!") 

 
 

# Define Colors 

WHITE=[255,255,255] 

BLACK=[0,0,0] 

 
 

# Load images 

images = [] 

screen.fill(WHITE) 

for i in range(7): 

    image= pygame.image.load("ImagesHM\hangman"+str(i)+ ".png") 

    images.append(image) 

    # screen.blit(images[i],(80,100)) 

    # pygame.display.update() 

    # pygame.time.delay(500) 

# Words list 

gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware'] 

 
 

#Set up fonts 

TitleFont = pygame.font.SysFont("comicsans", 70) 
WordFont = pygame.font.SysFont("comicsans", 50) 
LetterFont = pygame.font.SysFont("comicsans", 30)


#Define letters for rectangular buttons
A= 65
Wbox= 30
dist= 10
letters= []#an array of arrays  [[x, y, ltr, boolean]]
#Define where to start our drawing 26 letters, 13 letters in each line
startx= round((WIDTH - (Wbox + dist)*13) /2)  #int function round
starty= 350
#Load the letters into our double array
for i in range(26):
    x= startx + dist*2+((Wbox + dist)*(i%13))
    y= starty + ((i//13)*(dist + Wbox * 2))
    letters.append([x, y, chr(A+i), True])


# function to update game and screen 
def updateScreen(displayWord,turns): 
    screen.fill(WHITE) 
    screen.blit(images[turns],(80,100)) 
    pygame.display.update() 
    pygame.time.delay(500) 
    textW=WordFont.render(displayWord, 1, BLACK) 
    screen.blit(textW,(350, 150)) 
    text=TitleFont.render("HANGMAN", 1, BLACK) 
    centerTitle=WIDTH/2-text.get_width()/2  #gets  the width of my screen/2 - width ofour text /2 
    screen.blit(text, (centerTitle,20)) 
    screen.blit(images[turns],(80,100)) 
    for letter in letters:
        x,y,ltr, see= letter
        if see:
            rect= pygame.Rect(x-Wbox/2, y-Wbox/2, Wbox, Wbox)
            pygame.draw.rect(screen, BLACK, rect, width=1)
            text= LetterFont.render(ltr, 1, BLACK)
            screen.blit(text, (x -text.get_width()/2, y -text.get_height()/2))
    pygame.display.update() 

def updateWord(word, guesses):  # function with a parameter to update word 
    displayWord = "" 
    for char in word: 
        if char in guesses: 
            displayWord += char+" " 
        else: 
            displayWord += "_ " 
    return displayWord 

def dis_message(message):
    screen.fill(WHITE)
    text= TitleFont.render(message, 1, BLACK)
    screen.blit(text, (200, 200))
    pygame.display.update()
    pygame.time.delay(2000)

word=random.choice(gameWords).upper
guesses= []
turns= 0  #should we conider controlling this number when he/she misses 
check = True 
while check: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            check = False 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, see= letter
                if see:
                    rect= pygame.Rect(x-Wbox/2, y-Wbox/2, Wbox, Wbox)
                    if rect.collidepoint(mx, my):    #if letter has been clicked
                        letter[3]=False
                        guesses.append(ltr)
                        if ltr not in word:
                            turns += 1



    displayWord= updateWord(word, guesses) 
    updateScreen(displayWord, turns) 
    won= True
    for letter in word:
        if letter not in guesses:
            won=False
            break
    if won:
        dis_message("You won!")
        break
    if turns == 6:
        dis_message("You lost.")
        break

pygame.quit() 
sys.exit() 