#Maria Suarez
#June 11th, 2021
#Word Game
# We are creating a list of words
# randomly select a word from the list for the user to guess
# Give the user some turns
# Show the word to the user with the characters guessed
#play the game as long as the userhas turns or has guessed the word

import random
import time
import os
import sys
import datetime

os.system("cls")
x= 1
name= ""
date= datetime.datetime.now()
todaysDATE= date.strftime("%x")

l1="***************************************"
l2="*             Word Game               *"
l3="*                                     *"
l4="*         1 - Play Game               *"
l5="*         2 - High Scores             *"
l6="*         3 - Exit Game               *"
l7="***************************************"

def pause():
    print("Do you want to play again?")
    answer1= input()
    answer1=answer1.upper()
    if "Y" in answer1:
        return True
    else:
        return False

def updateWORD(word, guesses):    #This is a function that needs a value --->
    for char in word:
            #char=char.count(word)                            #Found the string but unsure how to use it!
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end =" ")

def menu():
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    print(l6)
    print(l7)
    print("Please enter your selection from 1 to 3.")
    inputNUMBER= input()
    x= int(inputNUMBER)
    return x

fileNAME= "Word_Game_1_HighScores.txt"

def getSCORES(score):
    os.system("cls")
    time.sleep(0.5)
    FILE= open(fileNAME, "r")
    print(FILE.read())
    input("Enter when you would like to stop viewing scores.")
    FILE.close()

def updatedSCORES(score):
    FILE = open(fileNAME, "a")
    line= "ON " + str(todaysDATE) + " - " + name + " HAD A SCORE OF " + str(score)
    FILE.write(line)
    FILE.write("\n")
    FILE.close


playersLIST= ["Lebron", "MJ", "Curry", "KD", "Granger", "Kobe", "Kareem", "Magic", "Hakeem", "Oscar", "Dirk", "Luka"]


def playGAME():
    score= 0
    answer= input("Do you want to guess a word?")
    answer=answer.upper()

    while "Y" in answer:
        print("Good luck", name, "!")
        word= random.choice(playersLIST)
        counter= len(word)
        print(word)
        turns= 10  # should we consider controlling this number when he/she misses?
        guesses=""
        updateWORD(word, guesses)
        while turns>0 and counter >0:
            newGUESS=input("\n Give me a letter.")
            if newGUESS not in word:
                turns -= 1
                print("Wrong.  You have", turns, "guesses left.")
            else:
                amount= word.count(newGUESS)
                counter -=amount
                print("Nice guess!")
                guesses += newGUESS
            updateWORD(word, guesses)
        if(counter==0):
            print("You guessed right!")
            score += 1
            print(score)
        else:
            print("Oops! Better luck next time!")
            print(score, "score is")
        answer= input("Would you like to play again?").upper()
    updatedSCORES(score)
    return score

while x !=3:
    x= menu()
    if x==1:
        convert= True
        while convert:
            name=input("What is your name?")
            score= playGAME()
            convert= pause()

    if x==2:
        getSCORES(score)
        
    if x==3:
        print("Thank you for playing.")
        



