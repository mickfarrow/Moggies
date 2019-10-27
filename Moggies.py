#main menu
    

def writeMenu():
    print("Main Menu-")
    print("Option A: 1 to 24 months")
    print("Option B: 3 to 18 years")
    print("Option X: exit menu")

    option = (input("Select menu option (Enter A, B or X): "))
    print("")
    return option

def writeResult(lifeStage, humanAge):
    print("")
    print ("Your cat is at life stage:", lifeStage)
    print ("Human age in years:", humanAge)
    print("")

option = writeMenu().upper()

while option not in "X":
    if option == "A":
        catAge = int(input("Enter cat age in months: "))
        if catAge < 4:
            humanAge = catAge
            writeResult("Kitten", humanAge)
            option = writeMenu().upper()
        elif catAge > 3 and catAge < 8:
            humanAge = catAge + 4
            writeResult("Kitten", humanAge)
            option = writeMenu().upper()
        elif catAge > 7 and catAge < 25:
            humanAge = catAge + 3
            writeResult("Junior", humanAge)
            option = writeMenu().upper()

    elif option == "B":
        catAge = int(input("Enter cat age in years: "))
        catThree = 3
        humanAge = (catAge - catThree) * 4 + 28
        lifeStage = "Geriatric"
        if catAge >= 3 and catAge <= 6:
            lifeStage="Prime"
        elif catAge >= 7 and catAge <= 10:
            lifeStage="Mature"
        elif catAge >= 11 and catAge <= 14:
            lifeStage="Senior"
        writeResult(lifeStage, humanAge)
        option = writeMenu().upper()
        







