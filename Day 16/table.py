# Import libraries
from prettytable import PrettyTable

# Create table
x = PrettyTable()

# Row by row
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)

# Create Table
y = PrettyTable()

# All rows at once
y.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
y.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

print(y)

table = PrettyTable()

table.field_names = ["Serial No.", "Name", "Type"]
table.add_rows(
    [
        [1, "Chespin", "Grass"],
        [2, "Quilladin", "Grass"],
        [3, "Chesnaught", "Grass , Fighting"],
        [4, "Fennekin", "Fire"],
        [5, "Braixen", "Fire"],
        [6, "Delphox", "Pychic"],
        [7, "Froakie", "Water"],
        [8, "Frogadier", "Water"]
    ]
)

print(table)
