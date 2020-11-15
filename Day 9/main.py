programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)

for key in programming_dictionary.keys():
    print(key)

for value in programming_dictionary.values():
    print(value)

for key, value in programming_dictionary.items():
    print(f"{key}:{value}")
