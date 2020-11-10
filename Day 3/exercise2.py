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
    bmi = round(float(weight)/(float(height)**2))

    if bmi < 18.5:
        print(f"Your BMI is {bmi} and you are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi} and you are normal.")
    elif bmi < 30:
        print(f"Your BMI is {bmi} and you are slightly overweight.")
    elif bmi < 35:
        print(f"Your BMI is {bmi} and you are obese.")
    else:
        print(f"Your BMI is {bmi} and you are clinically obese.")
except ValueError:
    print("Enter integer or float values only.")
