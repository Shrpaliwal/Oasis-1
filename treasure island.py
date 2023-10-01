print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("WELCOME TO TREASURE ISLAND!")

print("YOUR MISSION IS TO FIND THE TREASURE ")
choice1 = input('WHERE YOU WANT TO GO?"LEFT" OR "RIGHT".\n').lower()
if choice1 == "left":
    choice2 = input('you have come to lake. there is an island in the middle of the lake. Type "wait" to wait for a '
                    'boat. Type "swim" to swim accross.\n').lower()
    if choice2 == "wait":
        choice3 = input(
            'you reached to next level. which door you want to go? .Type "red" or "yellow" or "blue".\n').lower()
        if choice3 == "red":
            print("Its full off firee ohh noo ! you lost !")
        elif choice3 == "yellow":
            print("Its full of animals! ohh ohh you lost it !")
        elif choice3 == "blue":
            print("you found the treasure .... yupss you wonnn!!")
        else:
            print("you choose the door which do not exist  sorry!! game oveer!")
    else:
        print("you are attacked offfooooo!! game overrrr...!")

else:
    print("you fell into the hole!!! GAME OVER.")
