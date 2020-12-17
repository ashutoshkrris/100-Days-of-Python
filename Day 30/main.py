# Try/Except/Else/Finally

try:
    file = open("a_file.txt", "w")
except FileNotFoundError as err:
    print(err)
else:
    print("Else")
finally:
    file.close()

# Raise Exception
try:
    file_1 = open("a_file.txt")
except FileNotFoundError as err:
    print(err)
else:
    print("Else")
finally:
    file_1.close()
    raise KeyError("I raised it")
