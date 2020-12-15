"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files.
"""

with open("file1.txt") as file1:
    numbers1 = file1.readlines()

with open("file2.txt") as file2:
    numbers2 = file2.readlines()

result = [int(number.strip()) for number in numbers1 if number in numbers2]

# Write your code above 👆

print(result)
