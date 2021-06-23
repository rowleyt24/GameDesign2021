#Thomas Rowley
#6/16/21
#How to read files per line
#How to make a list from a file
#How to manipulateb the elements to find what we need

import sys
import os
import time

os.system("cls")

file= "asdfre.txt"
FILE= open(file, "r")
content= FILE.read()  #is string with full content of the file
print(content)
FILE.close
FILE= open(file, "r")
content_List= FILE.readlines()  #is a list of each line of the text file
print(content_List)
FILE.close()
for element in content_List:
    print("line: ", element)
    elem_list= element.split()
    print(elem_list)
    time.sleep(1)
#How do we put reorder our score file from highest to lowest
