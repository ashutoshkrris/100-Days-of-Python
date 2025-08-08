# Step 1

import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter among the word_list: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

if guess == chosen:
    print("you guessed Right")
else:
    print("you guessed Wrong")
