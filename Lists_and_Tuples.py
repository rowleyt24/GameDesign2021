#Thomas Rowley
# We are learning about lists and tuples
# Learning their functions and looping with lists

#How to use a module or library by importing

import random

myFruit=["apples", "berries", "mangos", "pineapples", "bananas"]
print(myFruit)
for fruit in myFruit:
        print(fruit)

for fruit in myFruit: #for each element of the array get the element
    print(fruit, end=" , ")

print()

counter= len(myFruit)  # length of your list is one more than your last index
#finding a random number to be the index to select randint()
index= random.randint(0, counter-1)
print("your lucky fruit is", myFruit[index])

#random method choice()
word=random.choice(myFruit)
print("Your random fruit is", word)
for x in range (0,counter-1):
    print(myFruit[x], end=" , ")

print(myFruit[counter-1])  #print the last element

if "apples" in myFruit:
    print("Yes you got apples")
    myFruit.remove("apples")
    print(myFruit)
myFruit.insert(0, "kiwi")
myFruit.insert(2, "papaya")
myFruit.append("dragonfruit")
print(myFruit)

fruity=("apple", "pears", "banana")  #tiple
print("tuple", fruity)
temp= list(fruity)       #list
print("list", temp)
temp.insert(1, "kiwi")
fruity=tuple(temp)
print("tuple modified", fruity)
print("list modified", temp)
for element in fruity:
        print(element)