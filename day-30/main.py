# try:
#     file = open("a_file.txt")
#     a_dictionary = {'key': 'value'}
#     print(a_dictionary['key'])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
try_again = True
while try_again:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        try_again = False

# apply on day-29
