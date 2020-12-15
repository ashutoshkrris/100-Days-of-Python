"""
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(f"{key} : {value}")


import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    print(row.student)

"""

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


# TODO 1. Create a dictionary in this format:
import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
words_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word : ").upper()

result = [words_dict[letter] for letter in user_word]
print(result)
