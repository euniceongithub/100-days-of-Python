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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_or_right = input(
    "You are at a crossroad. You must either go left or right. Type 'left' or 'right' to choose your path.\n"
).lower()

if left_or_right == "left":
    swim_or_wait = input(
        "Congratulations! You didn't die. You are now at a lake with an island in the middle. Do you swim to the island or do you wait?. Type 'wait' or 'swim' to choose your path.\n"
    ).lower()
    if swim_or_wait == "wait":
        which_door = input(
            "You're doing so good! You're now at a house with 3 doors. One is red, one is yellow and the other is blue. Which door do you choose? Type 'red', 'yellow' or 'blue' to indicate your choice.\n"
        ).lower()
        if which_door == "yellow":
            print("Huray! You won! Enjoy the treasure.")
        elif which_door == 'blue':
            print("You were eaten by beasts. So close! Game over.")
        elif which_door == 'red':
            print("Seriously? You just got burned by fire. Game over.")
        else:
            print("Not an option. Game over.")
    else:
        print("Oh no! You were eaten alive by trout. Game over.")

else:
    print("Oops! You fell into a hole. Game over so soon")
