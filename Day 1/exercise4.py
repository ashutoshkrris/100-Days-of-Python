'''Write a program that switches the values stored in the variables a and b.'''

a, b = map(int, input().split(" "))
a, b = b, a
print(a, b)
