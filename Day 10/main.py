# Functions with Outputs
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    f"Result: {formated_f_name} {formated_l_name}"


# Storing output in a variable
formatted_name = format_name(
    input("Your first name: "), input("Your last name: "))
print(formatted_name)
# or printing output directly
print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))

# Already used functions with outputs.
length = len(formatted_name)

# Return as an early exit


def format_name(f_name, l_name):
    """Take a first and last name and format it 
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
