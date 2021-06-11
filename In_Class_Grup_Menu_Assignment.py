#Thomas Rowley
#Modifying Quentin Balestri's code
# while loop
# conditional
# functions --> peices of code we can reuse
# to declare a function you must use the keyword def give a name to the funtion ()
#global variables
l1="********************************"
l2="*           My game            *"
l3="*                              *"
l4="*    1 - Capitalize            *"
l5="*    2 - Uppercase             *"
l6="*    3 - Lowercase             *"
l7="*    4 - Find index of char    *"
l8="*    5 - Split                 *"
l9="*    6 - Translate             *"
l10="*    7 - Exit Game             *"
l11="********************************"

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
    print(l9)
    print(l10)
    print(l11)
    print("Please enter your selection from 1 to 7")
    inputNumber = input()
    x = int(inputNumber)
    return x

def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False



def option1():
    print("Capitalize Chosen")
    print("Please enter a phrase in lowercase.")
    answer=input()   #input is a function returns a string
    print(answer.capitalize()) #is a method of strings and you have to refer with a period.


def option2():
    print("Uppercase Chosen")
    print("Please enter a phrase in lowercase.")
    answer=input()   #input is a function returns a string
    print(answer.upper()) #is a method of strings and you have to refer with a period.


def option3():
    print("Lowercase Chosen")
    print("Please enter  a phrase in all uppercase.")
    answer=input()   #input is a function returns a string
    print(answer.lower()) #is a method of strings and you have to refer with a period.
    

def option4():
    print("Index of Character Chosen")
    print("Enter a phrase, with a character you would like to know the position of.")
    answer=input()
    print("Which character would you like to know the location of?")
    answer1=input()
    completeINDEX= answer.index(answer1)
    print("The position is", completeINDEX, ".")
      

def option5():
    print("Split Chosen")
    print("Enter a phrase thats words you would like to be seperated.")
    answer= input()
    completeSPLIT= answer.split()
    print(completeSPLIT)
    

def option6():
    print("Translate Chosen")
    print("Make a dictionary with two ASCII codes that you would like to switch with each other.")
    letter1= input()
    letter2=input()
    dictionary= {letter1: letter2}
    print("What phrase would you like to translate?")
    answer= input()
    print(answer.translate(dictionary))
    


while x != 7:   #loop is ocnditioned to an event
    x = menu()       #call a function
    if(x==1):                      #if statement are selection or branching 
        convert= True      #Boolean variable
        while convert:
            option1()
            convert= pause()

    if(x==2):
        convert= True
        while convert:
            option2()
            convert= pause()

    if(x==3):
        convert= True
        while convert:
            option3()   #function call
            convert= pause()

    if(x==4):
        convert= True
        while convert:
            option4()
            convert= pause()

    if(x==5):
        convert= True
        while convert:
            option5()
            convert= pause()

    if(x==6):
        convert= True
        while convert:
            option6()
            convert= pause()

    if(x==7):
        print("Thank you for playing!")

print("Goodbye!")