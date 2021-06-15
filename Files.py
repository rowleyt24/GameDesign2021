#Thomas Rowley
#We are going to learn how to use files

import os
import sys
import time

#using time to pause your games

print("Hello")
time.sleep(1)
print("there.")

def readFILE():
    file= input("What is the name of the file? ")
    if os.path.exists(file):
        PEN= open(file, "r")
        #prints the whole file
        print(PEN.read())
    else:
     print("The file does not exist. Thank you!")

fileNAME= "ThomasGame.txt"
if os.path.exists(fileNAME):
    time.sleep(1)
    print("Sorry that file exists.")
else:
    FILE= open(fileNAME, "w")
    FILE.write("********   THIS IS THOMAS'S FILE   ********")
    FILE.close()
    time.sleep(1)
    FILE= open(fileNAME, "r")
    print(FILE.read())
    FILE.close()
File= open("ThomasGame.txt", "a")
newline= "\n \n WHat ever"
File.write(newline)
File.close()