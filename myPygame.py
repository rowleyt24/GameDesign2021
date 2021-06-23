import pygame, time, sys

pygame.init()
pygame.time.delay(100)
WIDTH= 600
HEIGHT= 400
#create the object
bg= pygame.image.load("Images/courtBACKGROUND.jpg")
dROSE= pygame.image.load("Images/roseSPRITE.jpg")
##create object to open window
screen= pygame.display.set_mode((WIDTH, HEIGHT))

white= (255, 255, 255)
black= (0, 0, 0)
red= (255, 0, 0)
purple= (171, 18, 222)

screen.fill(white)   #changes color of display
pygame.display.set_caption("My Game")  #Change title on the screen and also can change icon
pygame.display.update()  #what does this do?  Updates  the screen

#you must always... ALWAYS
check= True
x= 200
y= 200
rad= 30
hbox, wbox= 20, 20
rect= pygame.Rect(x, y, hbox, wbox)  #creates a rectangle
rect1= pygame.Rect(x, y, hbox, wbox)   
jumpCHECK= False
jump= 10

while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check= False
    speed= 5
    keyboardPRESS= pygame.key.get_pressed()   #checking what key is pressed
    if keyboardPRESS[pygame.K_LEFT]:   #moving left on x (-)
        rect.x -= speed
        x -= speed
    if keyboardPRESS[pygame.K_RIGHT]:
        rect.x += speed
    #check if we are going to jump
    
    if not jumpCHECK:
        if keyboardPRESS[pygame.K_UP]:
            rect.y -= speed
            y  += speed
        if keyboardPRESS[pygame.K_DOWN]:
            rect.y += speed
        if keyboardPRESS[pygame.K_SPACE]:
            jumpCHECK= True
    else: 
        if jump >=0 -10:
            rect.y -=(jump*abs(jump))/2
            jump -=1
        else:
            jump = 10
            jumpCHECK= False
    if keyboardPRESS[pygame.K_i]:
        rect1.y -= speed
    if keyboardPRESS[pygame.K_k]:
        rect1.y += speed
    if keyboardPRESS[pygame.K_l]:
        rect1.x += speed
    if keyboardPRESS[pygame.K_j]:
        rect1.x -= speed
    
    if rect.x < 0: rect.x=0
    if rect.x > WIDTH-wbox: rect.x = WIDTH-wbox
    if rect.y < 0: rect.y=0
    if rect.y > HEIGHT-hbox: rect.y = HEIGHT-hbox
    if rad < 0: rad=1
    if rad > WIDTH-x: rad = WIDTH-x

    if rect1.x < 0: rect.x=0
    if rect1.x > WIDTH-wbox: rect.x = WIDTH-wbox
    if rect1.y < 0: rect.y=0
    if rect1.y > HEIGHT-hbox: rect.y = HEIGHT-hbox

    if rect.colliderect(rect1):
        rect.x -=3
        rect1.x +=3
    
    screen.fill(white)
    screen.blit(bg, (0, 0))
    screen.blit(dROSE, (x, y))
    pygame.draw.rect(screen, (black), rect)
    pygame.draw.rect(screen, (black), rect1)
    pygame.draw.circle(screen, (black), (x+50, y+50), rad, 2)
    if keyboardPRESS[pygame.K_w]:
        rad += speed
    if keyboardPRESS[pygame.K_s]:
        rad -= speed
    pygame.display.update()
    pygame.time.delay(30)
pygame.quit()
