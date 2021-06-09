#Thomas Rowley
#Modifying Quentin Balestri's code
# while loop
# conditional
# functions --> peices of code we can reuse
# to declare a function you must use the keyword def give a name to the funtion ()
#global variables
l1="**************************"
l2="*       My game          *"
l3="*                        *"
l4="*    1 - Level1          *"
l5="*    2 - Level2          *"
l6="*    3 - Scores          *"
l7="*    4 - Exit Game       *"
l8="**************************"

x=1

def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print(l8)
    print("Please enter your selection from 1 to 4")
    inputNumber = input()
    x = int(inputNumber)
    return x

def score():
    print("Scores Chosen")
    print(l1)
    print("*        Scores          *")
    print(l3)
    print("*    1 - ???- 999        *")
    print("*    2 - ???- 876        *")
    print("*    3 - ???- 745        *")
    print(l3)
    print(l8)       


while x != 4:   #loop is ocnditioned to an event
    x = menu()       #call a function
    if(x==1):                      #if statement are selection or branching 
        print("Level 1 Chosen")
    if(x==2):
        print("Level 2 Chosen")
    if(x==3):
        score()   #function call

print("Goodbye thank you for playing!")