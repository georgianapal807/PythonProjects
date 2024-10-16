#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

result = [phonetic_alphabet[letter] for letter in user_input]
print(result)


