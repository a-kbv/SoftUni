import re

data = input()
word = input()

words = re.findall(rf"\b{word}\b", data, re.IGNORECASE)
print(len(words))