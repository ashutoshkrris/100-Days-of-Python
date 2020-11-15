# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name="None"):
    print(f"Hello {name} !")
    print("I am main.py")
    print("I am here to greet you.")

greet()

# args and kwargs

def greet_with(*args, **kwargs):
    print(args)
    print(kwargs)

greet_with("Hello","Ashutosh", name="None")