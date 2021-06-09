introTEXT = "My Game Menu"
menulevelONE = "  Level One "
menulevelTWO = "  Level Two "
menuPRINTSCORES = "Print Scores"
menuEXITGAME = "  Exit Game "


print("*************************************")
print("*", "          ", introTEXT, "         ", "*")
print("*", "          ", "            ", "         ", "*")
print("*", "          ", "            ", "         ", "*")
print("*", "          ", menulevelONE, "         ", "*")
print("*", "          ", menulevelTWO, "         ", "*")
print("*", "          ", menuPRINTSCORES, "         ", "*")
print("*", "          ", menuEXITGAME, "         ", "*")
print("*", "          ", "            ", "         ", "*")
print("*************************************")

print()
print()
print()
print("Type a number 1-4 corresponding with the menu selections.")

answer = int(input())

while answer!= 4:
    if answer == 1:
        print("Level One")
        answer = "changed"
    
    if answer == 2:
        print("Level Two")
        answer = "changed"

    if answer == 3:
        print("Print Scores")
        answer = "changed"

    print("*************************************")
    print("*", "          ", introTEXT, "         ", "*")
    print("*", "          ", "            ", "         ", "*")
    print("*", "          ", "            ", "         ", "*")
    print("*", "          ", menulevelONE, "         ", "*")
    print("*", "          ", menulevelTWO, "         ", "*")
    print("*", "          ", menuPRINTSCORES, "         ", "*")
    print("*", "          ", menuEXITGAME, "         ", "*")
    print("*", "          ", "            ", "         ", "*")
    print("*************************************")

    answer = int(input())
print("Good job!")

