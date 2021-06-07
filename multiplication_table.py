#Thomas Rowley 
#6/4/2021
#Printing a multiplication table.
# Using print statements
# inout --> variable is a cntainer to keep data (need valid and unique name)
base = 2
var2 = 7
print (1 * base)
print (2 * base)
print (3 * base)
print (4 * base)
print (5 * base)
print (6 * base)
print (7 * base)
print (8 * base)
print (9 * base)
print (10 * base)
#repetition think **looping**
for x in range(1, 11):  #beginning of range is included, end of range is not
     print (x * base, end = "   ")
base = 3
print ()
for x in range(1, 11):
    print (x * base, end = "   ")
base = 4
print ()
for x in range(1, 11):
    print (x * base, end = "   ")
#when we have multiple repetetians we can use veral loops
#sometimes they can be nested loops
for var in range(1, 11):
    print ()
    for x in range(1, 11):
        print (x * var, end = "   ")
