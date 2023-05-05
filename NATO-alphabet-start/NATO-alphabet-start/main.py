# NATO alphabet translator

import pandas

# Read data from csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from the data
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
