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

answer = str(input())

while "1" in answer:
    print(menulevelONE)
    answer = "changed"

while "2" in answer:
    print(menulevelTWO)
    answer = "changed"

while "3" in answer:
    print(menuPRINTSCORES)
    answer = "changed"

while "4" in answer:
    print("Are you sure you want to go?")
    answer = "changed"
    quitANSWER = str(input())

while "yes" in quitANSWER:
    print("Goodbye.")
    quitANSWER = "changed"

while "no" in quitANSWER:
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

    answer = str(input())
    quitANSWER = "changed"
