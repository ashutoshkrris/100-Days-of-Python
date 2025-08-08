'''Write a program that switches the values stored in the variables a and b.'''

x, y = map(int, input().split(" "))
x, y = y, x
print(x, y)
