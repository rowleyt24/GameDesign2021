import random, os, sys, datetime, time

def menu():
    print("***********************")
    print("* Terminal Battleship *")
    print("*                     *")
    print("*     Level One       *")
    print("*     Level Two       *")
    print("*    Level Three      *")
    print("*                     *")
    print("*       Scores        *")
    print("*      Quit Game      *")
    print("*                     *")
    print("***********************")

    print()
    print()
    print()

    print("Instructions- Type in a X and Y value for the assumed location of a Battleship with Y running from the right side of the screen counting up from 0, and X running from botton to top counting up from 0.")

    answer= int(input("Type a number between 1-5 to select a level, scores, ore quit game."))
    return answer
    

def make_random_ships(num_ships):
    random_values= []
    while True:
        
        y = random.randint(0, HEIGHT - 1)
        x = random.randint(0, WIDTH - 1)
        if (x,y) not in random_values:
            random_values.append((y,x))
        if len(random_values) == num_ships:
            break
    return random_values

file= "ReTry_Final_Project\Final_Project.txt"
def printSCORES():
    FileRead=open(file,'r')     
    print(FileRead.read())
    input("Press enter to continue.")     
    FileRead.close  


def updateSCORES():     
    FileWrite=open(file,'a')     
    line=NAME +  "SCORED A SCORE OF" + WINS    
    FileWrite.write("\n"+line)     
    FileWrite.close


def print_grid(grid):
    for coord in grid: 
        for val in coord:
            print(val,end="")
        print("")



ship_locations= []

answer= menu()
while answer != 5:
    if answer == 1:

        NAME= input("What is your name?")

        HEIGHT = int(input("How tall would you like your grid to be?\n"))
        WIDTH = int(input("How wide would you like your grid to be?\n"))
        NUM_SHIPS = int((HEIGHT * WIDTH)*.10) 
        grid = list()
        WINS = 0
        LOSSES = 0
        MAX_LOSSES = int((HEIGHT * WIDTH)*.20) 
        
        #setting up the game
        ship_locations = make_random_ships(NUM_SHIPS)
        print("Cheat Sheet")
        print(ship_locations)

        for i in range(0, HEIGHT): 
            line = list(" -"*WIDTH) 
            grid.append(line)

        print_grid(grid)



        while True: 
            shotx= int(input(f"What X value would you like to hit, it must be less than {WIDTH}\n"))
            shoty = int(input(f"What Y value would you like to hit, it must be less than {HEIGHT}\n"))
            if shotx < 0 or shotx >= WIDTH:
                print("ERROR. You may not pick a value greater than the width.")
                continue
            if shoty < 0 or shoty >= HEIGHT:
                print("ERROR. You may not pick a value greater than the height.")
                continue

            hit = False 
            for shipY, shipX in ship_locations: 
                if shipX == shotx and shipY == shoty: 
                    WINS += 1
                    grid[shipY][shipX] = "X"
                    hit = True 
                    break 

            if hit == False: 
                LOSSES += 1
                grid[shoty][shotx] = "O"
                print(f"Nice Try. But you have missed. You have {MAX_LOSSES-LOSSES} left")
            else: 
                print(f"Great Job! That was a hit! at {shipX}, {shipY} There are {NUM_SHIPS-WINS} ships left!")

            # PRINT GRID 
            print_grid(grid)
            if LOSSES == MAX_LOSSES: 
                print("GAME OVER!  Maybe next time.")
                break 
            if WINS == NUM_SHIPS: 
                print("You hit all of the ships!")
                updateSCORES()
                break 
            
    if answer== 2:
        HEIGHT = int(input("How tall would you like your grid to be?\n"))
        WIDTH = int(input("How wide would you like your grid to be?\n"))
        NUM_SHIPS = int((HEIGHT * WIDTH)*.05) 
        grid = list()
        WINS = 0
        LOSSES = 0
        MAX_LOSSES = int((HEIGHT * WIDTH)*.20) 
        
        #setting up the game
        ship_locations = make_random_ships(NUM_SHIPS)
        print("Cheat Sheet")
        print(ship_locations)

        for i in range(0, HEIGHT): 
            line = list(" -"*WIDTH) 
            grid.append(line)

        print_grid(grid)



        while True: 
            shotx= int(input(f"What X value would you like to hit, it must be less than {WIDTH}\n"))
            shoty = int(input(f"What Y value would you like to hit, it must be less than {HEIGHT}\n"))
            if shotx < 0 or shotx >= WIDTH:
                print("ERROR. You may not pick a value greater than the width.")
                continue
            if shoty < 0 or shoty >= HEIGHT:
                print("ERROR. You may not pick a value greater than the height.")
                continue

            hit = False 
            for shipY, shipX in ship_locations: 
                if shipX == shotx and shipY == shoty: 
                    WINS += 1
                    grid[shipY][shipX] = "X"
                    hit = True 
                    break 

            if hit == False: 
                LOSSES += 1
                grid[shoty][shotx] = "O"
                print(f"Nice Try. But you have missed. You have {MAX_LOSSES-LOSSES} left")
            else: 
                print(f"Great Job! That was a hit! at {shipX}, {shipY} There are {NUM_SHIPS-WINS} ships left!")

            # PRINT GRID 
            print_grid(grid)
            if LOSSES == MAX_LOSSES: 
                print("GAME OVER!  Maybe next time.")
                break 
            if WINS == NUM_SHIPS: 
                print("You hit all of the ships!")
                updateSCORES()
                break

    if answer== 3:
        HEIGHT = int(input("How tall would you like your grid to be?\n"))
        WIDTH = int(input("How wide would you like your grid to be?\n"))
        NUM_SHIPS = int((HEIGHT * WIDTH)*.025) 
        grid = list()
        WINS = 0
        LOSSES = 0
        MAX_LOSSES = int((HEIGHT * WIDTH)*.10) 
        
        #setting up the game
        ship_locations = make_random_ships(NUM_SHIPS)
        print("Cheat Sheet")
        print(ship_locations)

        for i in range(0, HEIGHT): 
            line = list(" -"*WIDTH) 
            grid.append(line)

        print_grid(grid)



        while True: 
            shotx= int(input(f"What X value would you like to hit, it must be less than {WIDTH}\n"))
            shoty = int(input(f"What Y value would you like to hit, it must be less than {HEIGHT}\n"))
            if shotx < 0 or shotx >= WIDTH:
                print("ERROR. You may not pick a value greater than the width.")
                continue
            if shoty < 0 or shoty >= HEIGHT:
                print("ERROR. You may not pick a value greater than the height.")
                continue

            hit = False 
            for shipY, shipX in ship_locations: 
                if shipX == shotx and shipY == shoty: 
                    WINS += 1
                    grid[shipY][shipX] = "X"
                    hit = True 
                    break 

            if hit == False: 
                LOSSES += 1
                grid[shoty][shotx] = "O"
                print(f"Nice Try. But you have missed. You have {MAX_LOSSES-LOSSES} left")
            else: 
                print(f"Great Job! That was a hit! at {shipX}, {shipY} There are {NUM_SHIPS-WINS} ships left!")

            # PRINT GRID 
            print_grid(grid)
            if LOSSES == MAX_LOSSES: 
                print("GAME OVER!  Maybe next time.")
                break 
            if WINS == NUM_SHIPS: 
                print("You hit all of the ships!")
                updateSCORES()
                break

    if answer== 4:
        printSCORES()
        break

    if answer== 5:
        print("Thank you for playing!")
    




    
    
    



    







