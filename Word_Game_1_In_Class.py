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

playersLIST= ["Lebron", "MJ", "Curry", "KD", "Granger", "Kobe", "Kareem", "Magic", "Hakeem", "Oscar", "Dirk", "Luka"]
answer= input("Do you want to guess a word?")
name=input("What is your name?")
answer=answer.upper()
while "Y" in answer:
    print("Good luck", name, "!")
    word= random.choice(playersLIST)
    counter= len(word)
    print(word)
    turns= 10  # should we consider controlling this number when he/she misses?
    guesses=""
    while turns>0 and counter >0:
        for char in word:
            #char=char.count(word)                            #Found the string but unsure how to use it!
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end =" ")
        newGUESS=input("\n Give me a letter.")
        if newGUESS not in word:
            turns -= 1
            print("Wrong.  You have", turns, "guesses left.")
        else:
            counter -= 1
            print("Nice guess!")
        guesses += newGUESS

    answer= input("Would you like to play again?").upper()
print(name, "thank you for playing!")
