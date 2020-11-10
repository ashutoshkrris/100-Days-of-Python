'''
You are going to write a program that tests the compatibility between two people. We're going to use the super scientific method recommended by BuzzFeed.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

name_string = (name1+name2).lower()

t = name_string.count("t")
r = name_string.count("r")
u = name_string.count("u")
e = name_string.count("e")

l = name_string.count("l")
o = name_string.count("o")
v = name_string.count("v")
e = name_string.count("e")

true = t+r+u+e
love = l+o+v+e

true_love = int(str(true)+str(love))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}")
