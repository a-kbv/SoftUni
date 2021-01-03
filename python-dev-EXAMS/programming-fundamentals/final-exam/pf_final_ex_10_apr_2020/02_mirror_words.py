
""""IMPORTANT 40/100 in judge"""

import re

string_input = input()

valid_pattern = r'[A-Za-z]{3,}\1\1[A-Za-z]{3,}\1'

matched = re.finditer(valid_pattern, string_input)

matched_list = [el[0] for el in matched]

if len(matched_list) > 0:
    print(f"{len(matched_list)} word pairs found!")
else:
    print("No word pairs found!")

mirrored_words = {}
for el in matched_list:
    word = el.split(el[0])[1]
    mirror_word = el.split(el[0])[3]
    if word == mirror_word[::-1]:
        mirrored_words[word] = mirror_word

if len(mirrored_words) >0:
    print(f"The mirror words are: \n"
          f"{', '.join(f'{key} <==> {value}' for key, value in mirrored_words.items())}")
else:
    print("No mirror words!")
