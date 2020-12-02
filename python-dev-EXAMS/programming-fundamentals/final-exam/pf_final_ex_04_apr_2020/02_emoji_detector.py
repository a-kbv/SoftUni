# https://judge.softuni.bg/Contests/Practice/Index/2302#1

# import re
#
# def cool_treshold(text):
#     '''
#     :param text: input
#     :return: returns all numbers in the text myltiplied by each other
#     '''
#     cool_th = 1
#     for el in text:                                    # for each char in text
#         if el.isnumeric():                             # checks if char is digit
#             cool_th *= int(el)                         # multiplies resut by digit
#     return cool_th
#
# text = input()                                         # user input string
#                                                        # regex patter and object
#
# # pattern = r'([*]{2})[A-Z][a-z]{2,}([*]{2})|([:]{2})[A-Z][a-z]{2,}([:]{2})' # old pattern
#
# # pattern = r'([:]{2}|[*]{2})([A-Z][a-z]{2,})\1'
#
# pattern = r'([:]{2}|[*]{2})[A-Z][a-z]{2,}\1'           # optimised pattern
# test = re.finditer(pattern, text)                      # creating object
# emojis = [(el.group(0)) for el in test]                # manipulating object to get the emojis
#
# cool_th = cool_treshold(text)                          # calculated cool treshold
# cool_emojis = []                                       # list of all emojis with higher treshhold than the cool treshold
#
# print(f"Cool threshold: {cool_th}")
# print(f"{len(emojis)} emojis found in the text. The cool ones are:")
#
# for el in emojis:                                      # calculates the sum of ascii of cool emojis
#     sum_el = sum([ord(x) for x in el if not x == ':'])
#     if sum_el >= cool_th:                              # if sum of ascii bigger than cool treshold
#         cool_emojis.append(el)                         # append to cool_emojis
#
# print('\n'.join(cool_emojis))                          # print the list as string on new lines


import re

string_input = input()

emojis_pattern = r'([:]{2}|[*]{2})[A-Z][a-z]{2,}\1'
numbers_pattern = r'\d'

emojis_matches = re.finditer(emojis_pattern, string_input)
numbers = re.finditer(numbers_pattern, string_input)

emojis_list = []
for element in emojis_matches:
    element = element[0].strip()
    emojis_list.append(element)

numbers_list = []
for num in numbers:
    numbers_list.append(int(num[0]))

threshold = 1
for x in numbers_list:
    threshold = threshold * x

print(f'Cool threshold: {threshold}')
print(f'{len(emojis_list)} emojis found in the text. The cool ones are:')
for emoji in emojis_list:
    char_sum = 0
    for char in emoji:
        if char.isalpha():
            char_sum += ord(char)
    if char_sum > threshold:
        print(f'{emoji}')