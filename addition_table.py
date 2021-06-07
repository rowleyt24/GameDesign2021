print("What number would you like to make an addition table for?")
additor = int(input())
print(type(additor))
print("Addition Table", additor)
print()
for x in range(1, 11):
    resolved = additor+x
    print(additor, "+", x, "=", (resolved))
    