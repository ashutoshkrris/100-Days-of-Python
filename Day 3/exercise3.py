'''
Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. 

This is how you work out whether if a particular year is a leap year.

On every year that is evenly divisible by 4 **except** every year that is evenly divisible by 100 **unless** the year is also evenly divisible by 400
'''

try:
    year = int(input("Please enter the year: "))
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"The year {year} is a Leap Year")
            else:
                print(f"The year {year} is NOT a Leap Year")
        else:
            print(f"The year {year} is a Leap Year")
    else:
        print(f"The year {year} is NOT a Leap Year")
        
except ValueError:
    print("Please enter the year in integer format only.")

