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

combined = (name1 + name2).lower()

# Count TRUE letters
t = combined.count("t")
r = combined.count("r")
u = combined.count("u")
e1 = combined.count("e")
true = t + r + u + e1

# Count LOVE letters
l = combined.count("l")
o = combined.count("o")
v = combined.count("v")
e2 = combined.count("e")
love = l + o + v + e2

score = int(str(true) + str(love))

print(f"Your love score is {score}")
