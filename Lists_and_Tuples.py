#Thomas Rowley
# We are learning about lists and tuples
# Learning their functions and looping with lists

myFruit=["apples", "berries", "mangos", "pineapples", "bananas"]
print(myFruit)
for fruit in myFruit:
        print(fruit)

for fruit in myFruit: #for each element of the array get the element
    print(fruit, end=" , ")

print()

counter= len(myFruit)  # length of your list is one more than your last index

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