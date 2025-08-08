'''
ROLLERCOASTER RIDE

Possible if : 
- height >= 120cm

- age < 12 : $ 5
- age 12-18 : $7
- age > 18 : $12

- photo : + $3 
'''

print("Welcome to the Rollercoaster Ride!")

height = int(input("What is your height in cms? : "))
age = int(input("Please enter your age in years: "))
photo = input("Do you want framed picture of your ride (Y/N): ").upper()

price = 0

if height >= 120:
    if age < 12:
        price += 5
    elif age < 18:
        price += 7
    else:
        price += 12

    if photo == "Y":
        price += 3

    print(f"Total price for your ride is ${price}")
else:
    print("Sorry! You must be at least 120 cm tall to ride.")
