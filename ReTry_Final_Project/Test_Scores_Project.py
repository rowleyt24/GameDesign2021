import sys, os


# def printSCORES():
#     file= "ReTry_Final_Project\Final_Project.py"
#     File=open(file,'r')     
#     print(File.read())     
#     File.close  

def readFILE():
    file= "ReTry_Final_Project\Final_Project.txt"
   
    PEN= open(file, "r")
    #prints the whole file
    print(PEN.read())

readFILE()

