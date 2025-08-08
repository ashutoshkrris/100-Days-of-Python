'''
You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
'''

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, separated by a comma: ")
names = namesAsCSV.split(",")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
payer = random.choice(names)

print(f"{payer} is going to buy the meal today!️")
