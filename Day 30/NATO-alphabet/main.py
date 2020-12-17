import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
words_dict = {row.letter: row.code for (index, row) in data.iterrows()}

game_is_on = True
while game_is_on:
    user_word = input("Enter a word : ").upper()
    try:
        result = [words_dict[letter] for letter in user_word]
    except KeyError:
        print("Please enter text only.")
    else:
        print(result)
        game_is_on = False
