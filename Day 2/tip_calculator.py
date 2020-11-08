# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

bill = input("What is your total bill? ")
persons = input("In how many persons is the bill to be splitted? ")
tip_rate = input(
    "What percent of bill do you wish to pay as tip : 10, 12 or 15 ? ")
try:
    amount = (float(bill)/int(persons)) * ((100+int(tip_rate))/100)
    print(f"You need to pay ${round(amount,2)} per person.")

except ValueError:
    print("Please enter float or integer values only.")
