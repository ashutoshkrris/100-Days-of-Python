'''
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
'''

size = input("Choose your pizza size (S/M/L): ").upper()
add_pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
extra_cheese = input("Do you want extra cheese? (Y/N): ").upper()

bill = 0

# Base price
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid pizza size entered!")
    exit()

# Pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# Extra cheese
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

