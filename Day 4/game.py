# ROCK PAPER SCISSOR game

import random
list = ["Rock","Paper","Scissors"]
user = int(input("Choose your turn (0, 1, 2 for rock, paper, scissor respectively): "))
print(f"you chose {list[user]}")
com_choice = random.randint(0,2)
print(f"the computer chose {list[com_choice]}")
if user == 0:
    if com_choice == 0:
        print("Draw")
    elif com_choice ==1:
        print("you lost")
    else:
        print("you won")
elif user == 1:
    if com_choice == 1:
        print("Draw")
    elif com_choice ==2:
        print("you lost")
    else:
        print("you won")
        
else:
    if com_choice == 2:
        print("Draw")
    elif com_choice ==0:
        print("you lost")
    else:
        print("you won")
