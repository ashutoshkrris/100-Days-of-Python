'''
ROLLERCOASTER RIDE

Possible if : 
- height >= 120cm

- age < 12 : $ 5
- age 12-18 : $7
- age > 18 : $12

- photo : + $3 
'''

height = int(input("What is your height in cms? : "))

if height >= 120:
    bill = 0
    age = int(input("How old are you ? : "))
    if age <= 12:
        bill += 5
    elif age < 18:
        bill += 7
    else:
        bill += 12

    photo = input("Do you want photo? : ")
    if photo == "Y":
        bill += 3

    print(f"Your total bill is {bill}.")
else:
    print("You are not eligible for the rollercoaster ride.")
