#Thomas Rowley
#Test for word game 1

import time
import os
import sys
import datetime

name= "Thomas"
#name= name.upper
score= 10
date= datetime.datetime.now()

fileNAME= "Word_Game_1_HighScores.txt"
FILE = open(fileNAME, "w")
line= "ON " + str(date) + " - " + name + " HAD A SCORE OF " + str(score)
FILE.write(line)
FILE.write("\n")
FILE.close
time.sleep(0.5)
FILE= open(fileNAME, "r")
print(FILE.read())
input("Enter when you would like to stop viewing scores.")
FILE.close()