# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

bill = input("What is your total bill? ")
persons = input("In how many persons is the bill to be splitted? ")
tip_rate = input(
    "What percent of bill do you wish to pay as tip : 10, 12 or 15 ? ")
try:
    share = ((float(bill)/int(persons))*(1+(float(tip_rate)/100)))
    print("Each person should pay",round((share),2))
except ValueError:
    print("please enter the value in correct format")
