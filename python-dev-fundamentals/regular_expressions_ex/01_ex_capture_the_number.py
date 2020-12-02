import re

data = input()
string = ""
while not data == "":
    string+=data
    data = input()
numbers = re.findall(r"\d+", string)
print(' '.join(numbers))