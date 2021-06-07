#Thomas Rowley 
#6/4/2021
#Printing a multiplication table.
#Asking the user which table
#input --> user
#input --> input()
# Using print statements
# inout --> variable is a cntainer to keep data (need valid and unique name)
print("What is the base?")
base = int(input())
print(type(base))
print("Multiplication Table", base)
print()
for x in range(1, 11):
    resolved = base*x
    print(base, "X", x, "=", (resolved))

