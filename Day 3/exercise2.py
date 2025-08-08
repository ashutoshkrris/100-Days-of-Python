'''
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- Over 25 but below 30 they are slightly overweight
- Over 30 but below 35 they are obese
- Above 35 they are clinically obese.
'''

height = input("Enter height in metres : ")
weight = input("Enter weight in kgs : ")

try:
    BMI = float(float(weight)/(float(height)*float(height)))
    print(BMI)
    if BMI< 18.5:
        print("you are underweight")
    elif BMI<25:
        print("you are Normalweight")
    elif BMI <30:
        print("you are Obese")
    else :
        print("you are clinically Obese")
except ValueError:
    print("please enter only float values")
