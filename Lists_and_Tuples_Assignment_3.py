#Thomas Rowley
#  insert elements either appending or inserting
# 2 delete an element either by value or by index
# 3  find if something in the list
# 4  Find the index where an element is in the list
# 5 reverse th eorder of the array
x=1

l1="**************************************"
l2="*              My game               *"
l3="*                                    *"
l4="*    1 - Insert Element              *"
l5="*    2 - Delete Element              *"
l6="*    3 - Find Element in List        *"
l7="*    4 - Find Index of Element       *"
l8="*    5 - Reverse Order of List       *"
l9="*    6 - Exit Game                   *"
l10="* List: MJ, Lebron, Curry, Kawhi, KD *"
l11="*                                    *"
l12="**************************************"

playersLIST=["MJ", "Lebron", "Curry", "Kawhi", "KD"]

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
    print(l12)
    print("Please enter your selection from 1 to 6")
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

def addELEMENT():
    print("Add element to list.")
    print("What basketball player would you like to add?")
    answer= input()
    print("What position would you like this to be in the list?")
    answer1= int(input())
    playersLIST.insert(answer1, answer)
    print("Here is the new list.")
    print(playersLIST)

def deleteELEMENT():
    print("Delete an element from the list.")
    print("What basketball player do you want to remove from the list?")
    print(playersLIST)
    answer= input()
    playersLIST.remove(answer)
    print("Here is the new list.")
    print(playersLIST)

def findELEMENT():
    print("Find something in the list.")
    print("What would you like to find in the list.")
    print(playersLIST)
    answer = input()
    if answer=="MJ":
        print("Your search is in the list.")
    if answer !="MJ":
        print("Your search is not contained in the list.")

    if answer=="Lebron":
        print("Your search is in the list.")
    if answer !="Lebron":
        print("Your search is not contained in the list.")

    if answer=="Curry":
        print("Your search is in the list.")
    if answer !="Curry":
        print("Your search is not contained in the list.")

    if answer=="Kawhi":
        print("Your search is in the list.")
    if answer !="Kawhi":
        print("Your search is not contained in the list.")

    if answer=="KD":
        print("Your search is in the list.")
    if answer !="KD":
        print("Your search is not contained in the list.")

def findINDEX():
    print("Find the index of an element.")
    print(playersLIST)
    print("Insert the element you would like to index.")
    answer = str(input())
    print(playersLIST.index(answer))

def reverseLIST():
    print("Reverse the order of the list.")
    print(playersLIST)
    print("Press enter to reverse the order of the list.")
    answer= input()
    playersLIST.reverse()
    print(playersLIST)

while x !=6:
    x = menu()
    if x==1:
        convert=True
        while convert:
            addELEMENT()
            convert= pause()

    if x==2:
        convert=True
        while convert:
            deleteELEMENT()
            convert= pause()

    if x==3:
        convert=True
        while convert:
            findELEMENT()
            convert= pause()

    if x==4:
        convert=True
        while convert:
            findINDEX()
            convert= pause()

    if x==5:
        convert=True
        while convert:
            reverseLIST()
            convert= pause()

    if x==6:
        print("Goodbye thank you for playing!")
