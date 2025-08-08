'''
Write a program that works out whether if a given number is an odd or even number.
'''

try:
    sum = int(input("enter the no. to check: "))
    if sum %2 ==0:
        print(f"the no.{sum} is even")
    else :
        print(f"the no.{sum} is Odd")
except ValueError:
    print("please enter integer value only")
