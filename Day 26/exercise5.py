"""
You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celcius and converts it into degrees Farenheight.
"""

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: temperature*9/5 +32 for (day, temperature) in weather_c.items()}

print(weather_f)
