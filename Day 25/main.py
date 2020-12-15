# USING FILE HANDLING

# with open("weather_data.csv") as file:
#     data = file.readlines()

# print(data)

# USING CSV MODULE

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# USING PANDAS

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])

import pandas as pd

data = pd.read_csv("squirrel_data.csv")
gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
red_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, red_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
