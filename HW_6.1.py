# ДЗ 6.1. Діапазон букв

import string

# letters_range = "a-c"
# letters_range = "a-a"
letters_range = "a-Z"

letters = string.ascii_letters

first_letter = letters.find(letters_range[0])
second_letter = letters.find(letters_range[-1])

print(letters[first_letter:second_letter + 1])

# lst_letters = []

# for i in range(first_letter, second_letter + 1):
#     lst_letters.append(letters[i])

# print("".join(lst_letters))
