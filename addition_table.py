print("What is the base?")
base = int(input())
print(type(base))
print("Multiplication Table", base)
print()
for x in range(1, 11):
    resolved = base*x
    print(base, "X", x, "=", (resolved))
    