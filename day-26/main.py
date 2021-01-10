# numbers = [1, 2, 3, 4, 5]
# new_numbers = [num+1 for num in numbers]
# range_list = [num*2 for num in range(1, 5)]

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)

# import random
# students_scores = {student: random.randint(1, 100) for student in names}
# print(students_scores)
# passed_students = {student: score for (
#     student, score) in students_scores.items() if score >= 60}
# print(passed_students)

import pandas

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# Loop through a data frame
# for (index, row) in student_data_frame.iterrows():
#     print(row.score)

alphabet_dict = {}
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
for (index, row) in alphabet_data.iterrows():
    alphabet_dict[row.letter] = row.code

user_name = input("What is your name? ")
print([alphabet_dict[char.upper()] for char in user_name])
