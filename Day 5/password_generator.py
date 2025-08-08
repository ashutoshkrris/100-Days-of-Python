# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



#Easy level (Non randomised order)
password = []

for char in range(1,nr_letters + 1):
    password += random.choice(letters)
for char in range(1, nr_symbols+1):
    password += random.choice(symbols)
for char in range(1,nr_numbers):
    password += random.choice(numbers)
password = ''.join(password)   
print(f"Easy password is: {password}")

#Tough level (Randomised Order)
Tpassword = []

for char in range(1,nr_letters + 1):
    Tpassword.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    Tpassword.append(random.choice(symbols))
for char in range(1,nr_numbers):
    Tpassword.append(random.choice(numbers))
    
random.shuffle(Tpassword)
Tpassword = ''.join(Tpassword)

print(f"Hard password is: {Tpassword}")
